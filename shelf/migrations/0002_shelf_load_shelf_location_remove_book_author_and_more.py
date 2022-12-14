# Generated by Django 4.1 on 2022-09-06 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelf',
            name='load',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shelf.book'),
        ),
        migrations.AddField(
            model_name='shelf',
            name='location',
            field=models.SlugField(default=''),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='shelf.author'),
        ),
    ]
