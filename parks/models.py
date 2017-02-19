import datetime

from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .rating import calculate_new_rating
from django.contrib.auth.models import User

class UserRating(models.Model):
    user = models.ForeignKey(User, null=True)
    park = models.ForeignKey('Park')
    rating = models.FloatField()
    class Meta():
        db_table = 'rating_tbl'
    @classmethod
    def create(cls, rating, park, user):
        rats = UserRating.objects.filter(user=user, park=park)
        if (not rats):
            newRating = cls(rating=rating, park=park, user=user)
            newRating.save()
            calculate_new_rating(park, rating, 0)
        else:
            for rat in rats:
                previousRating = rat
            else:
                preRatingFloat = previousRating.rating
                newRating = cls(rating=rating, park=park, user=user)
                previousRating.delete()
                newRating.save()
                calculate_new_rating(park, rating, preRatingFloat)

class Park(models.Model):
    park_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    official = models.IntegerField()
    address = models.CharField(max_length=100)
    neighbourhood = models.CharField(max_length=100)
    nurl = models.CharField(max_length=100)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    size = models.FloatField()
    washroom = models.IntegerField(null=True)
    special = models.IntegerField()
    advisory = models.IntegerField()
    problems = models.CharField(max_length=150, null=True)
    rating = models.FloatField()


    nearest1_id = models.IntegerField(null=True)
    nearest1_distance = models.FloatField(null=True)
    nearest1_name = models.CharField(max_length=100, null=True)
    nearest1_image = models.CharField(max_length=100, null=True)

    nearest2_id = models.IntegerField(null=True)
    nearest2_distance = models.FloatField(null=True)
    nearest2_name = models.CharField(max_length=100, null=True)
    nearest2_image = models.CharField(max_length=100, null=True)

    nearest3_id = models.IntegerField(null=True)
    nearest3_distance = models.FloatField(null=True)
    nearest3_name = models.CharField(max_length=100, null=True)
    nearest3_image = models.CharField(max_length=100, null=True)

    nearest4_id = models.IntegerField(null=True)
    nearest4_distance = models.FloatField(null=True)
    nearest4_name = models.CharField(max_length=100, null=True)
    nearest4_image = models.CharField(max_length=100, null=True)

    __callArg = []
    def update_rating(self, rating, user):
        UserRating.create(rating, self, user)

    def __str__(self):
        return self.name
    class Meta():
        db_table = 'parks_tbl'


class ParkFavorites(models.Model):
    user_id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.name
    class Meta():
        db_table = 'park_favorites_tbl'

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    favorite_park = models.CharField(max_length=1000, null=True)

    def __str__(self):
          return "%s's profile" % self.user

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

@receiver(pre_delete, sender=User)
def delete_profile_for_user(sender, instance=None, **kwargs):
    if instance:
        user_profile = UserProfile.objects.get(user=instance)
        user_profile.delete()
