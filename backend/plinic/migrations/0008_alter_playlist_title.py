# Generated by Django 3.2.14 on 2022-08-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plinic', '0007_auto_20220824_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='title',
            field=models.CharField(default='tempList', max_length=150),
        ),
    ]
