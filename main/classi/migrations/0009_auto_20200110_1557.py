# Generated by Django 3.0.1 on 2020-01-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classi', '0008_classeturnointerrogazione'),
    ]

    operations = [
        migrations.AddField(
            model_name='classeturnointerrogazione',
            name='numero_interrogati',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='classeturnointerrogazione',
            name='stato',
            field=models.IntegerField(default=0),
        ),
    ]
