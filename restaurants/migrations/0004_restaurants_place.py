# Generated by Django 5.1 on 2024-10-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaurants_adress_en_restaurants_adress_mk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='place',
            field=models.CharField(default='Gevgelija', max_length=100),
        ),
    ]
