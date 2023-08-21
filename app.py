from flask import Flask, request, jsonify
from rembg import remove

app = Flask(__name__)

@app.route('/remove_background', methods=['POST'])
def remove_background():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files['image']
        image_data = image_file.read()

        output_data = remove(image_data)

        return jsonify({"result": output_data.decode("latin-1")})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
