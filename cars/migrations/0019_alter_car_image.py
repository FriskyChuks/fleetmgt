# Generated by Django 3.2.6 on 2021-08-27 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0018_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, default='image/male.jpg', null=True, upload_to='image/'),
        ),
    ]
