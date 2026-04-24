from flask import Flask, request, jsonify
from src.pipeline.predict_pipeline import PredictPipeline
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Wine Quality Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']  # expects list of features
    pipeline = PredictPipeline()
    result = pipeline.predict(data)
    return jsonify({'prediction': float(result)})

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)