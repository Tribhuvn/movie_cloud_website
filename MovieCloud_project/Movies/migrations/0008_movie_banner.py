# Generated by Django 4.0.4 on 2022-08-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0007_movie_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(default='', upload_to='Movies_banner'),
            preserve_default=False,
        ),
    ]
