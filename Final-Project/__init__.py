import cv2
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

model = load_model('savedmodels.h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', message='No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            # Process the uploaded image and make predictions
            result = predict(filepath)
            return render_template('index.html', message='Prediction: ' + str(result))
    return render_template('index.html')

def predict(filepath):
    # Load the image, preprocess it, and make predictions
    # Replace this part with your actual preprocessing and prediction code
    img = cv2.imread(filepath)
    img = cv2.resize(img, (150, 150))  # Resize image to match model input size
    img = img.astype(np.float32) / 255.0  # Normalize pixel values to [0, 1]
    img = np.expand_dims(img, axis=0)   # Placeholder for image preprocessing
    prediction = model.predict(img)
    # Assuming your model outputs probabilities for each class
    class_names = ['COVID','Normal', 'virus']
    predicted_class = np.argmax(prediction, axis=1)
    return class_names[int(predicted_class)]

if __name__ == '__main__':
    app.run(debug=True)
