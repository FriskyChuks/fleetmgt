# Generated by Django 3.2.6 on 2021-08-26 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0005_auto_20210820_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='distance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
