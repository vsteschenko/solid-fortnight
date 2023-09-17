#!/usr/bin/env python3

import os
from PIL import Image

input_directory = ''
output_directory = ''
os.makedirs(output_directory, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_directory):
    input_path = os.path.join(input_directory, filename)
    
    # Check if the file is a valid image (JPEG, TIFF, etc.)
    try:
        with Image.open(input_path) as im:
            # Resize the image to 600x400 pixels
            im = im.resize((600, 400))

            # Construct the output path with .jpeg extension
            output_filename = os.path.splitext(filename)[0] + ".jpeg"
            output_path = os.path.join(output_directory, output_filename)

            # Save the processed image in JPEG format
            im.convert("RGB").save(output_path, "JPEG")
    
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")

print("Images resized and saved in", output_directory)
