from flask import Flask, request, jsonify
from rembg import remove
from flask_cors import CORS
import os
import base64




app = Flask(__name__)
CORS(app)  # This allows all origins, you can specify more options if needed


@app.route('/remove_background', methods=['POST'])
def remove_background():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files['image']
        image_data = image_file.read()

        output_data = remove(image_data)
         # Convert the processed image to base64
        base64_output = base64.b64encode(output_data).decode("utf-8")

        return jsonify({"result": base64_output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)