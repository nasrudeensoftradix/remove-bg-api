from flask import Flask, request, jsonify, Response
from rembg import remove
from flask_cors import CORS
import os



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

 # Return the processed image data as bytes
        # return jsonify({"result": output_data.decode("latin-1")})
        return Response(response=output_data, status=200, content_type='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)