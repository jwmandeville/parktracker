import shutil
import urllib
import zipfile
import os
import glob


def downloadExtractData():

    with urllib.request.urlopen("ftp://webftp.vancouver.ca/opendata/csv/csv_parks_facilities.zip") as response, open("parks.zip", 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    with zipfile.ZipFile('parks.zip', "r") as zfile:
        zfile.extractall("parks/data")
    os.remove('parks.zip')

    files = glob.glob('parks/data/*')
    for f in files:
        if f != 'parks/data/parks.csv' and f != r'parks/data\parks.csv' and f != 'parks/data/park_images.csv' and f!=\
                r'parks/data\park_images.csv':
                os.remove(f)
