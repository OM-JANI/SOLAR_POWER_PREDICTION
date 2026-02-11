from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("solar_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form["windspeed"]),
        float(request.form["sunshine"]),
        float(request.form["airpressure"]),
        float(request.form["radiation"]),
        float(request.form["airtemperature"]),
        float(request.form["humidity"])
    ]

    prediction = model.predict([features])[0]
    prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction_text=f"Predicted Solar Power Output: {prediction}"
    )

if __name__ == "__main__":
    app.run(debug=True)