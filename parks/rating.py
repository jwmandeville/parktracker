
import math
from django.db import models

def calculate_inital_rating(park):
    ratings = park.userrating_set.all()
    if not ratings:
        park.rating = 0
    else:
        total = 0
        for rating in ratings:
            total += rating.rating
        total = total/len(ratings)
        park.rating = total

def calculate_new_rating(park, rating, oldrating):
    # if (oldrating == 0):
    #     lenModifier = 0
    # else:
    #     lenModifier = 1
    # weighted_rating = (park.rating*(len(park.userrating_set.all())-lenModifier) - oldrating + rating)/len(park.userrating_set.all())
    # park.rating = (math.ceil(weighted_rating*100)/100)
    # park.save()
    ratings = park.userrating_set.all()
    if not ratings:
        park.rating = 0
    else:
        total = 0
        for rating in ratings:
            total += rating.rating
        total = total/len(ratings)
        park.rating = total
    park.save()
