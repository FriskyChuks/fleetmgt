# Generated by Django 3.2.6 on 2021-08-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0006_ride_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='destination',
            field=models.TextField(max_length=255),
        ),
    ]