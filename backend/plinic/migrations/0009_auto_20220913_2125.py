# Generated by Django 3.2.14 on 2022-09-13 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plinic', '0008_alter_playlist_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DateTimeField(),
        ),
    ]
