# Generated by Django 5.1 on 2024-08-26 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='category',
            new_name='adress',
        ),
        migrations.AddField(
            model_name='coffee',
            name='small_description',
            field=models.TextField(blank=True),
        ),
    ]
