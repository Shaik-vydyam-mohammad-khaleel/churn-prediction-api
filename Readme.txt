📊 Customer Churn Prediction API
🚀 Project Overview

This project predicts customer churn (whether a customer is likely to leave a service) using machine learning.
The trained model is deployed as a REST API on Google Cloud Run, making it accessible from anywhere.

⚙️ Features

Preprocessed customer data and trained ML model.
REST API built with Flask.
Containerized using Docker.
Deployed on Google Cloud Run.
Supports real-time churn predictions with probability scores.

🛠️ Tech Stack

Python 3.10
Flask – API framework
Scikit-learn – ML model training
Pandas / NumPy – Data preprocessing
Docker – Containerization
Google Cloud Build & Run – Deployment

📂 Project Structure

📂 churn-prediction-api
│── README.md              # Project overview, setup, usage, etc.
│── requirements.txt       # Python dependencies
│── Dockerfile             # Docker configuration
│── app.py                 # Flask API code
│── churn_model.pkl        # Trained ML model (optional: you can store in repo or cloud storage)
│── notebook/
│    └── model_building.ipynb   # Your Jupyter notebook for training & EDA
│── data/                  # (Optional) Sample dataset (not full dataset if it's big/private)

🔧 Setup Instructions

1️⃣ Clone the Repository
git clone <your-repo-url>
cd Main_ML_Projects

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Locally
python app.py

➡ API will run at http://127.0.0.1:5000/predict

🐳 Docker

Build Image
docker build -t churn-api .

Run Container
docker run -p 8080:8080 churn-api

➡ Access API at http://127.0.0.1:8080/predict

☁️ Deployment (Google Cloud Run)

Build & Push Image
gcloud builds submit --tag gcr.io/<PROJECT-ID>/churn-api


Deploy Service
gcloud run deploy churn-api \
    --image gcr.io/<PROJECT-ID>/churn-api \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated

Get the Service URL (e.g.):
https://churn-api-xxxxx.us-central1.run.app/predict

🔮 API Usage
Endpoint:
POST /predict

Request Body (JSON):
   {
     "age": 30,
     "subscriptiontype": "Premium",
     "tenure": 12
   }

Response:
   {
     "churn_prediction": 1,
     "churn_probability": 0.56
   }

✅ End-to-End Flow

Train churn model locally.
Save trained model (model.pkl).
Build API with Flask.
Containerize with Docker.
Deploy to Google Cloud Run.
Access API from anywhere to get predictions.

📌 Future Improvements

Automate CI/CD with GitHub Actions & Cloud Build.
Add monitoring & logging for requests.
Extend API to support batch predictions.

