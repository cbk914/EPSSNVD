import urllib.request
import datetime
import gzip
import os
import mysql.connector
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
            # Connect to MySQL server
            connection = mysql.connector.connect(
                host='hostname',
                user='username',
                password='password'
            )
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS epss_scores")
            # Connect to epss_scores database
            connection = mysql.connector.connect(
                host='hostname',
                user='username',
                password='password',
                database='epss_scores'
            )
            cursor = connection.cursor()
            # Create table
            cursor.execute("CREATE TABLE IF NOT EXISTS epss_scores (name VARCHAR(255), value INTEGER)")
            # Insert data
            with open(file_name.strip('.gz'), 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cursor.execute("INSERT INTO epss_scores (name, value) VALUES (%s, %s)", (row['name'], row['value']))
            connection.commit()
            print("File Loaded Successfully to MySQL")
