# Generated by Django 3.2.14 on 2022-07-31 18:07


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='plinic/profile_pic/%Y/%m/%d'),
        ),
    ]