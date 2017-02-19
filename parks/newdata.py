import csv
import sqlite3
from .distance_calc import distance
from .models import Park, UserRating
from .open import downloadExtractData
from .rating import calculate_inital_rating


def cleardb():
    db = sqlite3.connect('parkdb')
    cursor = db.cursor()
    cursor.execute('''DELETE FROM parks_tbl;''')
    cursor.execute('''DELETE FROM rating_tbl;''')
    cursor.execute('''VACUUM;''')
    db.commit()
    db.close()


def parse():
    downloadExtractData()
    dataReader = csv.reader(open('parks/data/parks.csv'), delimiter=',', quotechar='"')
    for row in dataReader:
        if row[0] != 'ParkID':  # Ignore the header row, import everything else
            park = Park()
            park.park_id = row[0]
            park.name = row[1]
            park.official = row[2]
            street_number = row[3]
            street = row[4]
            park.address = street_number + " " + street
            park.neighbourhood = row[9]
            park.nurl = row[10]

            # parse lat_long
            lat_long = row[7]
            lat_long_list = lat_long.split(",")
            park.lat = lat_long_list[0]
            park.long = lat_long_list[1]

            park.size = row[8]
            washroom = row[14]
            if washroom == "Y":
                park.washroom = 1
            else:
                park.washroom = 0
            special = row[13]
            if special == "Y":
                park.special = 1
            else:
                park.special = 0
            advisory = row[11]
            if advisory == "Y":
                park.advisory = 1
            else:
                park.advisory = 0
            park.__callArg = []
            calculate_inital_rating(park)
            park.save()
    parse_images()
    parse_nearest_parks()

def parse_images():
    image_parser = csv.reader(open('parks/data/park_images.csv'), delimiter=',', quotechar='"')
    for row in image_parser:
        if row[0] != 'park_id':  # Ignore the header row, import everything else
            image_url = "http://www.vancouver.ca/" + row[1]
            Park.objects.filter(park_id=row[0]).update(image_url=image_url)

def parse_nearest_parks():
    for park in Park.objects.all():
        lat1 = park.lat
        lon1 = park.long
        closest_parks = []
        for park2 in Park.objects.all():
            if (park2.park_id != park.park_id):
                lat2 = park2.lat
                lon2 = park2.long
                d = distance((lat1,lon1), (lat2, lon2))
                closest_parks.append([d, park2.park_id, park2.name, park2.image_url])
        closest_parks.sort()

        park.nearest1_distance = closest_parks[0][0]
        park.nearest1_id = closest_parks[0][1]
        park.nearest1_name = closest_parks[0][2]
        park.nearest1_image = closest_parks[0][3]

        park.nearest2_distance = closest_parks[1][0]
        park.nearest2_id = closest_parks[1][1]
        park.nearest2_name = closest_parks[1][2]
        park.nearest2_image = closest_parks[1][3]

        park.nearest3_distance = closest_parks[2][0]
        park.nearest3_id = closest_parks[2][1]
        park.nearest3_name = closest_parks[2][2]
        park.nearest3_image = closest_parks[2][3]

        park.nearest4_distance = closest_parks[3][0]
        park.nearest4_id = closest_parks[3][1]
        park.nearest4_name = closest_parks[3][2]
        park.nearest4_image = closest_parks[3][3]

        park.save()
