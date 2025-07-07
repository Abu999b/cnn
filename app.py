
from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import json
import requests
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
import logging
from datetime import datetime
from tensorflow.keras.models import load_model

# Constants
MODEL_PATH = 'model/inception_v3_finetuned_L2.h5'
MODEL_URL = 'https://huggingface.co/abubakar4u900/scalp-disease-inceptionv3/resolve/main/inception_v3_finetuned_L2.h5'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SECRET_KEY'] = 'your-secret-key-here'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

# Create required directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('model', exist_ok=True)

# Download model if not present
if not os.path.exists(MODEL_PATH):
    logger.info("Downloading model...")
    response = requests.get(MODEL_URL)
    with open(MODEL_PATH, 'wb') as f:
        f.write(response.content)
    logger.info("Model downloaded successfully.")

# Load model
model = load_model(MODEL_PATH)
conditions = [
    "acne-keloidalis", "alopecia-areata", "androgenic-alopecia",
    "discoid-lupus", "dissecting-cellulitis", "folliculitis-decalvans",
    "hirsutism", "hot-comb-alopecia", "lichen-planopilaris",
    "pseudopelade", "telogen-effluvium", "trichorrhexis-nodosa",
    "trichotillomania", "tufted-folliculitis"
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_disease_info():
    try:
        with open('disease_info.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning("disease_info.json not found. Using default data.")
        return {"dermatological_conditions": []}

def preprocess_image(image_path):
    try:
        image = Image.open(image_path)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image = image.resize((150, 150))
        image_array = np.array(image).astype(np.float32) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        return image_array
    except Exception as e:
        logger.error(f"Error preprocessing image: {str(e)}")
        raise

def predict_condition(image_array):
    try:
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class]) * 100
        return [{
            'condition': conditions[predicted_class],
            'confidence': confidence
        }]
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type.'}), 400

        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
        filename = timestamp + filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        image_array = preprocess_image(filepath)
        predictions = predict_condition(image_array)
        disease_info = load_disease_info()

        results = []
        for pred in predictions:
            condition_name = pred['condition']
            confidence = pred['confidence']
            disease_data = next((d for d in disease_info['dermatological_conditions']
                                 if d['name'].lower().replace(' ', '-') == condition_name), None)
            if disease_data:
                results.append({
                    'condition': condition_name,
                    'name': disease_data['name'],
                    'confidence': confidence,
                    'description': disease_data['description'],
                    'symptoms': disease_data['symptoms'],
                    'treatment': disease_data['treatment'],
                    'advice': disease_data['advice']
                })

        logger.info(f"Processed image: {filename}, Prediction: {results[0]['name'] if results else 'None'}")
        return jsonify({'success': True, 'filename': filename, 'predictions': results})

    except Exception as e:
        logger.error(f"Error processing upload: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.errorhandler(413)
def too_large(e):
    return jsonify({'error': 'File too large. Max size is 16MB.'}), 413

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(e):
    logger.error(f"Internal server error: {str(e)}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
