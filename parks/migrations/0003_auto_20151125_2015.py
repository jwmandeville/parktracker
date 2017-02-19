# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0002_userrating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorite_park',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='rating',
            field=models.FloatField(),
        ),
    ]
