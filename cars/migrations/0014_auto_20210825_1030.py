# Generated by Django 3.2.6 on 2021-08-25 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_carownerdriverregister_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='carownerdriverregister',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carownerdriverregister',
            name='next_of_kin_relationship',
            field=models.CharField(choices=[('spouse', 'Spouse'), ('brother', 'Brother'), ('sister', 'Sister'), ('father', 'Father'), ('mother', 'Mother'), ('cousin', 'Cousin'), ('nephew', 'Nephew'), ('niece', 'Niece'), ('uncle', 'Uncle'), ('aunt', 'Aunt'), ('neighbour', 'Neighbour'), ('son', 'Son'), ('daughter', 'Daughter'), ('son', 'Son')], default='brother', max_length=50),
            preserve_default=False,
        ),
    ]
