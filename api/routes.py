from flask import Blueprint, request, jsonify
from utils.predictor import predict_news

api = Blueprint('api', __name__)

@api.route('/analyze', methods=['POST'])
def analyze():

    data = request.json
    text = data.get("text")

    result, confidence = predict_news(text)

    return jsonify({
        "status": "success",
        "result": result,
        "confidence": confidence
    })