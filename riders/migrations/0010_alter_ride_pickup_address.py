# Generated by Django 3.2.6 on 2021-08-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0009_alter_ride_pickup_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='pickup_address',
            field=models.CharField(default='Keffi', max_length=255),
            preserve_default=False,
        ),
    ]
