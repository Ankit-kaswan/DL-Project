import os
import uuid
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.image_utils import decode_image
from cnnClassifier.pipeline.stage_07_prediction import PredictionPipeline
from cnnClassifier import logger


# Env variables for Flask unicode support
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

# Secret token to protect training route
TRAIN_SECRET = "your-secret-token"


# Route to home page
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


# Route to trigger training process
@app.route("/train", methods=['POST'])
@cross_origin()
def train_route():
    token = request.headers.get('Authorization')
    if token != f"Bearer {TRAIN_SECRET}":
        return jsonify({"error": "Unauthorized"}), 403

    # Trigger the training process (can be optimized)
    os.system("python main.py")
    return jsonify({"message": "Training done successfully!"})


# Route to handle prediction requests
@app.route("/predict", methods=['POST'])
@cross_origin()
def predict_route():
    try:
        image = request.json.get('image')
        if not image:
            return jsonify({"error": "No image provided"}), 400

        # Generate unique filename for the image
        unique_filename = f"{uuid.uuid4().hex}.jpg"
        decode_image(image, unique_filename)

        # Initialize the prediction pipeline and run prediction
        prediction_pipeline = PredictionPipeline(image_path=unique_filename)
        result = prediction_pipeline.main()

        # Clean up image file after prediction
        os.remove(unique_filename)

        return jsonify(result)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    try:
        logger.info("*******************")
        logger.info(">>> Flask app started <<<")
        app.run(host='0.0.0.0', port=5000)  # Run the app on port 5000
        logger.info(">>> Flask app completed <<<\n\nx==========x")
    except Exception as e:
        logger.exception("Error starting Flask app: %s", e)
        raise e
