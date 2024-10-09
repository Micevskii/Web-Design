# Generated by Django 5.1 on 2024-10-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blogs_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='category_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='category_mk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='description_mk',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='title_mk',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
