```python
from flask import Flask, request, render_template_string
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load Linear Regression model
MODEL_PATH = "linear_model(1).pkl"
model = joblib.load(MODEL_PATH)

# Complete HTML + CSS in one file
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Linear Regression Predictor</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body {
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 500px;
            background: rgba(255, 255, 255, 0.97);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
        }

        .header .icon {
            width: 70px;
            height: 70px;
            margin: auto;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            margin-bottom: 15px;
        }

        h1 {
            color: #222;
            font-size: 28px;
            margin-bottom: 8px;
        }

        .subtitle {
            color: #777;
            font-size: 14px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            color: #333;
            font-weight: bold;
            margin-bottom: 8px;
        }

        input {
            width: 100%;
            padding: 14px;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
            outline: none;
            transition: 0.3s;
        }

        input:focus {
            border-color: #667eea;
            box-shadow: 0 0 8px rgba(102, 126, 234, 0.25);
        }

        button {
            width: 100%;
            padding: 15px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-size: 17px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            border-radius: 12px;
            background: #f1f5ff;
            text-align: center;
            border: 1px solid #dbe4ff;
        }

        .result-title {
            color: #555;
            font-size: 14px;
            margin-bottom: 8px;
        }

        .prediction {
            color: #667eea;
            font-size: 30px;
            font-weight: bold;
        }

        .error {
            margin-top: 20px;
            padding: 15px;
            border-radius: 10px;
            background: #ffe9e9;
            color: #d63031;
            text-align: center;
        }

        .footer {
            text-align: center;
            margin-top: 25px;
            color: #999;
            font-size: 12px;
        }

        @media (max-width: 600px) {
            .container {
                padding: 25px;
            }

            h1 {
                font-size: 24px;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <div class="header">
        <div class="icon">📊</div>

        <h1>Linear Regression</h1>

        <p class="subtitle">
            Enter your input value to get a prediction
        </p>
    </div>

    <form method="POST">

        <div class="form-group">
            <label for="feature">
                Enter Feature Value
            </label>

            <input
                type="number"
                step="any"
                name="feature"
                id="feature"
                placeholder="Enter a value"
                required
            >
        </div>

        <button type="submit">
            Predict
        </button>

    </form>

    {% if prediction is not none %}

    <div class="result">

        <div class="result-title">
            Predicted Value
        </div>

        <div class="prediction">
            {{ prediction }}
        </div>

    </div>

    {% endif %}

    {% if error %}

    <div class="error">
        {{ error }}
    </div>

    {% endif %}

    <div class="footer">
        Powered by Flask & Linear Regression
    </div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    error = None

    if request.method == "POST":

        try:
            # Get input from user
            feature = float(request.form["feature"])

            # Convert input into 2D array
            input_data = np.array([[feature]])

            # Make prediction
            result = model.predict(input_data)

            # Get first prediction
            prediction = round(float(result[0]), 4)

        except Exception as e:
            error = "Prediction Error: " + str(e)

    return render_template_string(
        HTML,
        prediction=prediction,
        error=error
    )


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
```
