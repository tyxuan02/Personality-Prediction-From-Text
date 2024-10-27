from flask import Flask, render_template, request
from flask_cors import CORS
from model_predictor import ModelPredictor  # Import the model class

app = Flask(__name__)
CORS(app)

# Instantiate the model predictor globally
model_predictor = ModelPredictor()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() 
    input_type = data['inputType']
    input = ""

    # Check input type and retrieve text input
    if input_type == 'text':
        input = data['input']
    elif input_type == 'file':
        # todo
        input = data['input']
        
    # Predict MBTI type
    output = model_predictor.predict(input)

    return output

@app.route('/about', methods=['GET'])
def about():
    return "teretw"

if __name__ == '__main__':
    app.run()