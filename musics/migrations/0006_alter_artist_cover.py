# Generated by Django 4.2.7 on 2024-06-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0005_alter_artist_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='cover',
            field=models.ImageField(blank=True, default='images/covers/cover.jpeg', null=True, upload_to=''),
        ),
    ]