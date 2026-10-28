
from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__)

# Load saved model and preprocessing pipeline
try:
    model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
    pipeline = joblib.load(os.path.join(BASE_DIR, "pipeline.pkl"))
    MODEL_ERROR = None
    print("Model and pipeline loaded successfully!")

except Exception as error:
    model = None
    pipeline = None
    MODEL_ERROR = str(error)
    print("Model loading failed:", MODEL_ERROR)


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/style.css")
def style():
    return send_from_directory(FRONTEND_DIR, "style.css")


@app.route("/script.js")
def script():
    return send_from_directory(FRONTEND_DIR, "script.js")


@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": model is not None and pipeline is not None,
        "error": MODEL_ERROR
    })


@app.route("/api/predict", methods=["POST"])
def predict():
    if model is None or pipeline is None:
        return jsonify({"error": f"Model loading failed: {MODEL_ERROR}"}), 500

    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"error": "Valid JSON input is required"}), 400

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

        transformed = pipeline.transform(features)
        price = float(model.predict(transformed)[0])

        return jsonify({"predicted_price": round(price, 2)})

    except KeyError as error:
        return jsonify({"error": f"Missing field: {error}"}), 400
    except (TypeError, ValueError) as error:
        return jsonify({"error": f"Invalid input: {error}"}), 400
    except Exception as error:
        app.logger.exception("Prediction failed")
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))
    app.run(host="0.0.0.0", port=port, debug=False)
