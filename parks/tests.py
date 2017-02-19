from django.test import TestCase
import csv
from .rating import calculate_inital_rating
from .models import Park


class ParserTests(TestCase):
    def setUp(self):
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

        #global test variables
        self.park1 = Park.objects.get(pk=1)
        self.park100 = Park.objects.get(pk=100)
        self.park246 = Park.objects.get(pk=246)

    def test_parks_id (self):
        self.assertEquals(self.park1.park_id, 1)
        self.assertEquals(self.park100.park_id, 100)
        self.assertEquals(self.park246.park_id, 246)

    def test_parks_name (self):
        self.assertEquals(self.park1.name, "Arbutus Village Park")
        self.assertEquals(self.park100.name, "Champlain Heights Park")
        self.assertEquals(self.park246.name, "Creekway Park")

    def test_parks_address (self):
        self.assertEquals(self.park1.address, "4202 Valley Drive")
        self.assertEquals(self.park100.address, "3351 Maquinna Drive")
        self.assertEquals(self.park246.address, "2901 E Hastings Street")

    def test_parks_neighbourhood (self):
        self.assertEquals(self.park1.neighbourhood, "Arbutus Ridge")
        self.assertEquals(self.park100.neighbourhood, "Killarney")
        self.assertEquals(self.park246.neighbourhood, "Hastings-Sunrise")

    def test_parks_nurl (self):
        self.assertEquals(self.park1.nurl, "http://vancouver.ca/community_profiles/arbutus_ridge/index.htm")
        self.assertEquals(self.park100.nurl, "http://vancouver.ca/community_profiles/killarney/index.htm")
        self.assertEquals(self.park246.nurl, "http://vancouver.ca/community_profiles/hastings-sunrise/index.htm")

    def test_parks_lat (self):
        self.assertEquals(self.park1.lat, 49.249783)
        self.assertEquals(self.park100.lat, 49.215527)
        self.assertEquals(self.park246.lat, 49.288336)

    def test_parks_long (self):
        self.assertEquals(self.park1.long, -123.155250)
        self.assertEquals(self.park100.long, -123.032545)
        self.assertEquals(self.park246.long, -123.036982)

    def test_parks_size (self):
        self.assertEquals(self.park1.size, 1.41)
        self.assertEquals(self.park100.size, 7.84)
        self.assertEquals(self.park246.size, 8.0)

    def test_parks_washroom (self):
        self.assertEquals(self.park1.washroom, 0)
        self.assertEquals(self.park100.washroom, 0)
        self.assertEquals(self.park246.washroom, 0)

    def test_parks_official (self):
        self.assertEquals(self.park1.official, 1)
        self.assertEquals(self.park100.official, 1)
        self.assertEquals(self.park246.official, 1)

    def test_parks_special (self):
        self.assertEquals(self.park1.special, 0)
        self.assertEquals(self.park100.special, 0)
        self.assertEquals(self.park246.special, 0)

    def test_parks_advisory (self):
        self.assertEquals(self.park1.advisory, 0)
        self.assertEquals(self.park100.advisory, 0)
        self.assertEquals(self.park246.advisory, 0)
