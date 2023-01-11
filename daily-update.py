import urllib.request
import datetime
# Add ´0 0 * * * /usr/bin/python3 /path/to/file/daily-update.py´ to contrab
url = "https://epss.cyentia.com/epss_scores-current.csv.gz"
now = datetime.datetime.now()
file_name = "epss_scores-" + now.strftime("%Y-%m-%d") + ".csv.gz"
urllib.request.urlretrieve(url, file_name)

print("Succesfully downloaded as " + file_name)
except Exception as e:
    print("Error al descargar el archivo: " + str(e))
