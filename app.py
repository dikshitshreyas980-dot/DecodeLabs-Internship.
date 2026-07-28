import os
import json
import joblib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'model.pkl')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Load Model Pipeline lazily or at startup
model_pipeline = None
try:
    if os.path.exists(MODEL_PATH):
        model_pipeline = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Warning: Could not load model pipeline: {e}")

def load_json(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dataset', methods=['GET'])
def get_dataset():
    data = load_json('dataset_info.json')
    return jsonify(data)

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    data = load_json('metrics.json')
    return jsonify(data)

@app.route('/api/k-analysis', methods=['GET'])
def get_k_analysis():
    data = load_json('k_analysis.json')
    return jsonify(data)

@app.route('/api/predict', methods=['POST'])
def predict():
    if not model_pipeline:
        return jsonify({'error': 'Model not trained or not found.'}), 500
        
    try:
        req_data = request.get_json()
        
        # Validate inputs
        required_keys = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        for key in required_keys:
            if key not in req_data:
                return jsonify({'error': f'Missing required feature: {key}'}), 400
                
        # Extract features
        features = [
            float(req_data['sepal_length']),
            float(req_data['sepal_width']),
            float(req_data['petal_length']),
            float(req_data['petal_width'])
        ]
        
        # Predict
        prediction = model_pipeline.predict([features])[0]
        prediction_name = ['setosa', 'versicolor', 'virginica'][prediction]
        
        # Predict Proba if available
        probabilities = None
        if hasattr(model_pipeline, 'predict_proba'):
            probs = model_pipeline.predict_proba([features])[0]
            probabilities = {
                'setosa': round(float(probs[0]), 4),
                'versicolor': round(float(probs[1]), 4),
                'virginica': round(float(probs[2]), 4)
            }
            
        return jsonify({
            'predicted_class': int(prediction),
            'predicted_class_name': prediction_name,
            'probabilities': probabilities
        })
        
    except ValueError:
        return jsonify({'error': 'Invalid data types provided. Ensure all inputs are numbers.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
