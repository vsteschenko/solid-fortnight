#!/usr/bin/env python3
import requests
import os

# Define the URL of the web server for image uploads
server_url = ""

# Specify the directory where your JPEG images are located
image_directory = "/path/to/your/images"

# List all the files in the image directory
image_files = os.listdir(image_directory)

# Filter the list to include only JPEG files
jpeg_files = [file for file in image_files if file.endswith(".jpeg")]

# Loop through the JPEG files and upload each one
for jpeg_file in jpeg_files:
    with open(os.path.join(image_directory, jpeg_file), 'rb') as opened_file:
        response = requests.post(server_url, files={'file': opened_file})

    # Check if the upload was successful (HTTP status code 201)
    if response.status_code == 201:
        print(f"Successfully uploaded {jpeg_file} to the server.")
    else:
        print(f"Failed to upload {jpeg_file}. Server response status code: {response.status_code}")
