# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('park_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=100)),
                ('official', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('neighbourhood', models.CharField(max_length=100)),
                ('nurl', models.CharField(max_length=100)),
                ('lat', models.FloatField(null=True)),
                ('long', models.FloatField(null=True)),
                ('size', models.FloatField()),
                ('washroom', models.IntegerField(null=True)),
                ('special', models.IntegerField()),
                ('advisory', models.IntegerField()),
                ('problems', models.CharField(max_length=150, null=True)),
                ('rating', models.FloatField()),
                ('nearest1_id', models.IntegerField(null=True)),
                ('nearest1_distance', models.FloatField(null=True)),
                ('nearest1_name', models.CharField(max_length=100, null=True)),
                ('nearest1_image', models.CharField(max_length=100, null=True)),
                ('nearest2_id', models.IntegerField(null=True)),
                ('nearest2_distance', models.FloatField(null=True)),
                ('nearest2_name', models.CharField(max_length=100, null=True)),
                ('nearest2_image', models.CharField(max_length=100, null=True)),
                ('nearest3_id', models.IntegerField(null=True)),
                ('nearest3_distance', models.FloatField(null=True)),
                ('nearest3_name', models.CharField(max_length=100, null=True)),
                ('nearest3_image', models.CharField(max_length=100, null=True)),
                ('nearest4_id', models.IntegerField(null=True)),
                ('nearest4_distance', models.FloatField(null=True)),
                ('nearest4_name', models.CharField(max_length=100, null=True)),
                ('nearest4_image', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'parks_tbl',
            },
        ),
        migrations.CreateModel(
            name='ParkFavorites',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'park_favorites_tbl',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('favorite_park', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='user_profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('park', models.ForeignKey(to='parks.Park')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'rating_tbl',
            },
        ),
    ]
