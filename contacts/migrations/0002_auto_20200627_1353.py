# Generated by Django 3.0.7 on 2020-06-27 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 13, 53, 41, 104859)),
        ),
    ]
