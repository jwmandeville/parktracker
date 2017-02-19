# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrating',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
