#!/usr/bin/env python3

import os
import requests
import json

def catalog_fruit_data(url, description_dir):
    """
    This script catalogs fruit data from text files in the given directory and sends it to a specified URL.
    It converts the weight to an integer format.
    :param url: The URL to send the data to.
    :param description_dir: The directory containing fruit description text files.
    """
    for item in os.listdir(description_dir):
        fruit_data = {}
        filename = os.path.join(description_dir, item)
        
        with open(filename) as f:
            lines = f.readlines()
            description = ""
            
            for i in range(2, len(lines)):
                description += lines[i].strip('\n').replace(u'\xa0', u'')
            
            fruit_data["description"] = description
            fruit_data["weight"] = int(lines[1].strip('\n').strip('lbs'))
            fruit_data["name"] = lines[0].strip('\n')
            fruit_data["image_name"] = (item.strip('.txt')) + '.jpeg'
            
            print(fruit_data)
            
            if url:
                response = requests.post(url, json=fruit_data)
                print(response.request.url)
                print(response.status_code)

if __name__ == '__main__':
    # Specify the URL where fruit data will be sent
    api_url = 'https://your-fruit-api.com/catalog'
    
    # Get the current user (you can customize this if needed)
    user = os.getenv('USER')
    
    # Specify the directory containing fruit description text files
    description_directory = '/path/to/your/fruit/descriptions/'
    
    # Call the function to catalog and send fruit data
    catalog_fruit_data(api_url, description_directory)
