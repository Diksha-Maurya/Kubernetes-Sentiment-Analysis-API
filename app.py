# app.py
import os
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Loading the model once when the application starts.
# As is a resource-intensive operation, so we don't want to do it on every request.
# The 'pipeline' function from Hugging Face is the easiest way to use a pre-trained model.
print("Loading sentiment analysis model...")
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
print("Model loaded successfully!")


@app.route('/')
def home():
    return "<h1>Sentiment Analysis API</h1><p>Send a POST request to /analyze</p>"


@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "No 'text' field provided in the request."}), 400

    text_to_analyze = data['text']

    result = sentiment_pipeline(text_to_analyze)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)