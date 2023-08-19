# Importing Required Modules
from rembg import remove
from PIL import Image
import logging

# Store path of the image in the variable input_path
input_path = "/home/softrdix/Downloads/cr_em13_09.jpg"

# Store path of the output image in the variable output_path
output_path = "/home/softrdix/Downloads/gfgoutput.png"

# Processing the image
input = Image.open(input_path)

logging.info(input, "input")
# Removing the background from the given Image
output = remove(input)

# Saving the image in the given path
output.save(output_path)
