from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
import sys
import urllib.request
import os
import zipfile
from books_recommender.utils.util import read_yaml_file
from books_recommender.constant import *

#--testing logging--
#logging.info("Book System")

#--Checking custom Exception--
# try:
#   4/0
# except Exception as e:
#   logging.info(e)  # Default Exception
#   raise AppException(e, sys) from e # Custom Excepiton

#--testing logging--
# print(read_yaml_file("config/config.yaml"))

#print(CONFIG_FILE_PATH)

url = "https://github.com/tareqrahaman/Datasets/raw/main/book_data.zip"
local_path = "test_download.zip"

urllib.request.urlretrieve(url, local_path)
print(f"Downloaded {os.path.getsize(local_path)} bytes")
print(f"Is ZIP: {zipfile.is_zipfile(local_path)}")

# Check what's inside
with open(local_path, 'rb') as f:
    print(f"First 50 bytes: {f.read(50)}")