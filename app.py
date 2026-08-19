
` ```python ` aur last wala ` ``` ` **Python code ka part nahi hote**. Ye sirf ChatGPT/Markdown mein code formatting ke liye hote hain.

### ✅ `app.py` aise hona chahiye

First line directly Python code se start honi chahiye:

```python
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("linear_model(1).pkl", "rb"))

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Student Performance Prediction</title>
    </head>
    <body>
        <h1>Student Performance Prediction</h1>

        <form action="/predict" method="post">
            <input type="number" name="hours" placeholder="Study Hours" required>
            <input type="number" name="attendance" placeholder="Attendance" required>
            <button type="submit">Predict</button>
        </form>
    </body>
    </html>
    """

@app.route("/predict", methods=["POST"])
def predict():
    hours = float(request.form["hours"])
    attendance = float(request.form["attendance"])

    prediction = model.predict([[hours, attendance]])

    return f"<h1>Predicted Result: {prediction[0]}</h1>"

if __name__ == "__main__":
    app.run()
