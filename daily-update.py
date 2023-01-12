


# Add ´0 0 * * * /usr/bin/python3 /path/to/file/daily-update.py´ to contrab
import urllib.request
import datetime
import locale

url = "https://epss.cyentia.com/epss_scores-current.csv.gz"
now = datetime.datetime.now()
file_name = "epss_scores-" + now.strftime("%Y-%m-%d") + ".csv.gz"
urllib.request.urlretrieve(url, file_name)

print("Succesfully downloaded as " + file_name)
except Exception as e:
    print("Error downloading file: " + str(e))

if "CRON" not in os.environ:
    current_locale, encoding = locale.getdefaultlocale()
    if current_locale in ["es_ES", "es_MX", "es_PE", "es_VE"]:
        answer = input("¿Desea descomprimir el archivo? (s/n): ")
        if answer.lower() == "s":
            with gzip.open(gz_file_name, 'rb') as f_in:
                with open(file_name, 'wb') as f_out:
                    f_out.writelines(f_in)
            print(f"Archivo {gz_file_name} descomprimido y guardado como {file_name}")
    elif current_locale in ["fr_FR"]:
        answer = input("Voulez-vous décompresser le fichier? (o/n): ")
        if answer.lower() == "o":
            with gzip.open(gz_file_name, 'rb') as f_in:
                with open(file_name, 'wb') as f_out:
                    f_out.writelines(f_in)
            print(f"Archivo {gz_file_name} décompressé et enregistré en tant que {file_name}")
    elif current_locale in ["nl_NL"]:
        answer = input("Wilt u het bestand uitpakken? (j/n): ")
        if answer.lower() == "j":
            with gzip.open(gz_file_name, 'rb') as f_in:
                with open(file_name, 'wb') as f_out:
                    f_out.writelines(f_in)
            print(f"Bestand {gz_file_name} uitgepakt en opgeslagen als {file_name}")            
    else:
        answer = input("Do you want to uncompress the file? (y/n): ")
        if answer.lower() == "y":
            with gzip.open(gz_file_name, 'rb') as f_in:
                with open(file_name, 'wb') as f_out:
                    f_out.writelines(f_in)
            print(f"File {gz_file_name} uncompressed and saved as {file_name}")
