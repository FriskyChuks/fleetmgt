# Generated by Django 3.2.6 on 2021-08-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0008_alter_ride_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='pickup_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
