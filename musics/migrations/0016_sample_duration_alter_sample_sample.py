# Generated by Django 5.0.6 on 2024-06-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0015_rename_melodiy_melody'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='duration',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample',
            field=models.FileField(null=True, upload_to='samples'),
        ),
    ]