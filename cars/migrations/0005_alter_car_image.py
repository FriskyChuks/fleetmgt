# Generated by Django 3.2.6 on 2021-08-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210819_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(default='1.png', upload_to='core/static/assets/img/cars'),
        ),
    ]