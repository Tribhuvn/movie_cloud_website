# Generated by Django 4.0.4 on 2022-08-14 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0005_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
