from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)


@app.route("/remove_background", methods=["POST"])
def remove_background():
    try:
        # Get the uploaded image from the POST request
        uploaded_file = request.files["image"]

        if uploaded_file:
            # Process the uploaded image using rembg
            input_image = Image.open(uploaded_file)
            output_image = remove(input_image)

            # Save the output image to a BytesIO object
            output_io = io.BytesIO()
            output_image.save(output_io, format="PNG")
            output_io.seek(0)

            # Return the background-removed image as a response
            return send_file(output_io, mimetype="image/png")
        else:
            return "No image uploaded.", 400
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(debug=True)
