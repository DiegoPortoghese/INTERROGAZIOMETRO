# Generated by Django 3.0.1 on 2020-01-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classi', '0006_auto_20200108_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='alunni',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='numero_alunni',
        ),
        migrations.AlterField(
            model_name='classeoramateria',
            name='giorno_della_settimana',
            field=models.IntegerField(choices=[(0, 'NoneNone'), (1, 'Lunedì'), (2, 'Martedì'), (3, 'Mercoledì'), (4, 'Giovedì'), (5, 'Venerdì'), (6, 'Sabato'), (7, 'Domenica')], default=0, verbose_name='Giorno della settimana'),
        ),
    ]