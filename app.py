
from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__)

# Load the trained model and preprocessing pipeline
try:
    model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
    pipeline = joblib.load(os.path.join(BASE_DIR, "pipeline.pkl"))
    MODEL_ERROR = None
    print("Model and pipeline loaded successfully!")

except Exception as e:
    model = None
    pipeline = None
    MODEL_ERROR = str(e)
    print("Model loading error:", MODEL_ERROR)


# Serve the frontend HTML
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


# Serve CSS
@app.route("/style.css")
def style():
    return send_from_directory(FRONTEND_DIR, "style.css")


# Serve JavaScript
@app.route("/script.js")
def script():
    return send_from_directory(FRONTEND_DIR, "script.js")


# Check whether the model loaded
@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": model is not None and pipeline is not None,
        "error": MODEL_ERROR
    })


# Predict house price
@app.route("/api/predict", methods=["POST"])
def predict():
    if model is None or pipeline is None:
        return jsonify({
            "error": f"Model not loaded: {MODEL_ERROR}"
        }), 500

    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"error": "No valid input data received"}), 400

        features = pd.DataFrame([{
            "longitude": float(data["longitude"]),
            "latitude": float(data["latitude"]),
            "housing_median_age": float(data["housing_median_age"]),
            "total_rooms": float(data["total_rooms"]),
            "total_bedrooms": float(data["total_bedrooms"]),
            "population": float(data["population"]),
            "households": float(data["households"]),
            "median_income": float(data["median_income"]),
            "ocean_proximity": data["ocean_proximity"]
        }])

        processed_features = pipeline.transform(features)
        predicted_price = model.predict(processed_features)[0]

        return jsonify({
            "predicted_price": round(float(predicted_price), 2)
        })

    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400

    except Exception as e:
        app.logger.exception("Prediction failed")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting Housing Price Prediction app...")
    print("Website: http://127.0.0.1:8001")
    app.run(host="127.0.0.1", port=8001, debug=False)
