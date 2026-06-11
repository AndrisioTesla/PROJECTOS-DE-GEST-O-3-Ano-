import joblib

model = joblib.load("model/fake_news_model.pkl")

vectorizer = joblib.load("model/vectorizer.pkl")

def predict_news(news_text):

    text = vectorizer.transform([news_text])

    prediction = model.predict(text)

    confidence = abs(model.decision_function(text)[0])

    confidence = min(confidence * 10,100)

    if prediction[0] == 0:

        result = "FAKE NEWS"

    else:

        result = "NOTÍCIA VERDADEIRA"

    return result, round(confidence,2)