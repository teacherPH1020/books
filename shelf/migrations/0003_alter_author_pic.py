# Generated by Django 4.1 on 2022-09-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_shelf_load_shelf_location_remove_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='pic',
            field=models.ImageField(upload_to='author_pics/'),
        ),
    ]
