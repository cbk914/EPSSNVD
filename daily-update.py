#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: cbk914
# Add ´0 0 * * * /usr/bin/python3 /path/to/file/daily-update.py´ to contrab
import urllib.request
import datetime
import gzip
import os
from pymongo import MongoClient
import csv

url = "https://epss.cyentia.com/epss_scores-current.csv.gz"
now = datetime.datetime.now()
file_name = "epss_scores-" + now.strftime("%Y-%m-%d") + ".csv.gz"

try:
    urllib.request.urlretrieve(url, file_name)
    print("Succesfully downloaded as " + file_name)
except Exception as e:
    print("Error downloading file: " + str(e))

if "CRON" not in os.environ:
    answer = input("¿Uncompress the file? (y/n) ")
    if answer.lower() == "y":
        try:
            with gzip.open(file_name, 'rb') as f_in:
                with open(file_name.strip('.gz'), 'wb') as f_out:
                    f_out.writelines(f_in)
            print(f"File {file_name} uncompressed and saved as {file_name.strip('.gz')}")
        except Exception as e:
            print(f"Error uncompressing file: {str(e)}")
        try:
            client = MongoClient()
            db = client['epss-scores']
            collection = db.epss_scores

            with open(file_name.strip('.gz'), 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    collection.insert_one(row)
            print("File Loaded Successfully to Mongo DB")
        except Exception as e:
            print(f"Error Loading file to Mongo DB: {str(e)}")
else:
    print("CRON job detected, no interaction available")
