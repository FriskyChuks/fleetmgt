# Generated by Django 3.2.6 on 2021-08-20 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0002_alter_ride_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='user',
            new_name='rider',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='service',
        ),
    ]