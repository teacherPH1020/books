# Generated by Django 4.1 on 2022-09-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_book_ebook_alter_author_pic_alter_book_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ebook',
            field=models.FileField(null=True, upload_to='ebook/%Y/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pic',
            field=models.ImageField(null=True, upload_to='ebook/%Y/'),
        ),
    ]