# Generated by Django 3.0.1 on 2020-01-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200106_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_image',
            field=models.ImageField(null=True, upload_to='rooms/img/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='profile',
            name='complete_progress',
            field=models.IntegerField(default=0),
        ),
    ]
