from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load trained model
model = joblib.load("churn_model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Churn Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON input
        data = request.get_json()
        input_df = pd.DataFrame([data])

        # Ensure input has all model features
        missing_cols = set(model.feature_names_in_) - set(input_df.columns)
        for col in missing_cols:
            input_df[col] = 0  # fill missing columns with 0

        # Reorder columns to match training
        input_df = input_df[model.feature_names_in_]

        # Make prediction
        prob = model.predict_proba(input_df)[0][1]
        prediction = int(model.predict(input_df)[0])

        return jsonify({
            "churn_probability": round(float(prob), 2),
            "churn_prediction": prediction
        })

    except Exception as e:
        # Return error as JSON instead of crashing
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))  # Cloud Run provides PORT env var
    app.run(debug=True, host="0.0.0.0", port=port)

