# Generated by Django 4.2.7 on 2024-06-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0004_artist_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
