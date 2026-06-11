from flask import Flask, render_template, request

from utils.predictor import predict_news
from utils.database import init_db, save_analysis, get_all

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    news = request.form['news']

    result, confidence = predict_news(news)

    save_analysis(news, result, confidence)

    return render_template("result.html",
                           result=result,
                           confidence=confidence)


@app.route('/history')
def history():
    data = get_all()
    return render_template("history.html", data=data)


@app.route('/dashboard')
def dashboard():

    data = get_all()

    fake = sum(1 for d in data if d[2] == "FAKE NEWS")
    real = sum(1 for d in data if d[2] == "NOTÍCIA VERDADEIRA")

    return render_template("dashboard.html", fake=fake, real=real)

if __name__ == "__main__":
    app.run(debug=True)