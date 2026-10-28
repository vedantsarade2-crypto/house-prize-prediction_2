# 🏠 California Housing Price Prediction

An end-to-end Machine Learning web application that predicts estimated house values in California using the California Housing Dataset. The project combines a trained Random Forest regression model with a web-based frontend, allowing users to enter property details and receive an instant price estimate.

## 🌐 Live Demo

**Try the application here:**  
🔗 https://house-prize-prediction-2.vercel.app/

## 📌 Project Overview

House price prediction is a regression problem in Machine Learning. Property values depend on several factors, including geographical location, median income, housing age, number of rooms, population, and proximity to the ocean.

This project uses a trained Machine Learning model and a preprocessing pipeline to predict an estimated house value from user-provided inputs through a web interface.

The application is deployed on Vercel and provides a simple way to interact with the trained model without running Python code manually.

## ✨ Features

- 🏡 **House Price Prediction:** Estimate property values using a trained Random Forest regression model.
- 🌍 **Location-Based Inputs:** Enter longitude, latitude, and ocean proximity.
- 📊 **Housing Data Inputs:** Provide housing age, total rooms, bedrooms, population, households, and median income.
- ⚡ **Instant Predictions:** Submit the form and receive a model-generated estimate.
- 🎨 **Interactive Frontend:** A clean, responsive interface built with HTML and CSS.
- 🔗 **Backend Integration:** Connect the frontend to the Python prediction API.
- ☁️ **Cloud Deployment:** Access the application online through Vercel.

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Pandas | Organizing input features into a DataFrame |
| NumPy | Numerical computing dependency |
| Scikit-learn | Machine Learning model and preprocessing |
| Joblib | Loading saved model and pipeline files |
| Flask | Backend routes and prediction API |
| HTML5 | Webpage structure |
| CSS3 | Styling and responsive layout |
| JavaScript | Form handling and API communication |
| Vercel | Cloud deployment |
| Git & GitHub | Version control and source code hosting |

## 🤖 Machine Learning Model

The application uses a trained **Random Forest Regressor**, a supervised Machine Learning algorithm suitable for regression tasks.

The saved model and preprocessing pipeline are loaded from:

- `model.pkl` — trained prediction model.
- `pipeline.pkl` — preprocessing pipeline used to transform input features before prediction.

### How the prediction works

1. The user enters property and location details on the website.
2. JavaScript collects the input values.
3. The frontend sends the data to the Flask prediction API.
4. The backend converts the input into a Pandas DataFrame.
5. The saved preprocessing pipeline transforms the input features.
6. The trained Random Forest model generates a prediction.
7. The predicted value is returned to the frontend and displayed to the user.

## 📥 Input Features

The application uses nine input features.

| Feature | Description |
|---|---|
| `longitude` | Longitude of the geographical location |
| `latitude` | Latitude of the geographical location |
| `housing_median_age` | Median age of houses in the area |
| `total_rooms` | Total number of rooms in the area |
| `total_bedrooms` | Total number of bedrooms in the area |
| `population` | Population of the area |
| `households` | Number of households in the area |
| `median_income` | Median income, using the dataset's original scale |
| `ocean_proximity` | Categorical location relative to the ocean |

**Note:** Median income uses the dataset's original scale. For example, a value of `5` represents approximately $50,000 in median annual household income.

## 🔄 Project Workflow

```text
California Housing Dataset
          |
          v
Data Preparation & Preprocessing
          |
          v
Random Forest Model Training
          |
          v
Save Model and Pipeline
          |
          v
Build Web Frontend
          |
          v
Flask Prediction API
          |
          v
Deploy on Vercel
          |
          v
User Enters Property Details
          |
          v
Predicted House Value
```

## 📂 Project Structure

```text
house-prize-prediction_2/
│
├── frontend/
│   ├── index.html       # User interface
│   ├── style.css        # Website styling
│   └── script.js        # Form handling and API calls
│
├── app.py               # Flask backend and prediction API
├── model.pkl            # Trained Random Forest model
├── pipeline.pkl         # Saved preprocessing pipeline
├── housing.csv          # Housing dataset
├── requirements.txt     # Python dependencies
├── vercel.json          # Vercel configuration
├── .gitignore           # Files excluded from Git
├── main_new.py          # Original model development script
├── main_old.py          # Earlier development script
└── README.md            # Project documentation
```

*The structure above documents the main files used in the project. Optional development scripts and data files may differ depending on the version uploaded to GitHub.*

## ⚙️ Run the Project Locally

### Prerequisites

- Python 3.10 or a compatible Python version
- pip
- Git (optional)

### 1. Clone the repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd house-prize-prediction_2
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

### 5. Open the website

Visit:

http://127.0.0.1:8001/

The local port depends on the port configured in `app.py`.

## ☁️ Deployment

The application is deployed using Vercel.

General deployment workflow:

1. Push the project source files to a GitHub repository.
2. Import the repository into Vercel.
3. Configure the Python application and required dependencies.
4. Deploy the application.
5. Open the deployment URL and test the prediction form.

**Live application:** https://house-prize-prediction-2.vercel.app/

## 🔌 API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Serves the frontend |
| `/api/health` | GET | Checks backend and model-loading status |
| `/api/predict` | POST | Accepts property features and returns a prediction |

The prediction endpoint accepts JSON containing the nine input features and returns a JSON response with `predicted_price`.

## 🎯 Learning Outcomes

Through this project, I explored:

- Building a complete Machine Learning application.
- Understanding regression-based prediction.
- Preparing input features for a trained model.
- Saving and loading models with Joblib.
- Using Scikit-learn preprocessing pipelines.
- Integrating a frontend with a Python backend.
- Creating a prediction API with Flask.
- Deploying a Machine Learning application on Vercel.
- Organizing a project for GitHub and portfolio presentation.

## ⚠️ Limitations

- The output is an estimate generated by a Machine Learning model, not a formal property appraisal.
- Predictions depend on the training data, model quality, and supplied input values.
- The dataset reflects historical housing information and may not represent current market prices.
- The model's performance should be evaluated separately using appropriate regression metrics.

## 🚀 Future Improvements

- Evaluate and document model performance using MAE, RMSE, and R² score.
- Improve input validation and error handling.
- Add data visualizations and feature importance analysis.
- Compare Random Forest with other regression algorithms.
- Improve model monitoring and deployment reliability.
- Retrain the model using more recent and relevant data when available.

## 👨‍💻 Author

**Vedant Sarade**

Machine Learning | Python | Data Science

---

⭐ If you find this project interesting, consider starring the repository on GitHub.

**Disclaimer:** This application is developed for educational and demonstration purposes. Its predictions should not be treated as guaranteed property valuations or financial advice.
