# Generated by Django 3.2.6 on 2021-08-30 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_alter_car_image'),
        ('riders', '0012_alter_ride_service_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='service_class',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.rideserviceclass'),
        ),
    ]
