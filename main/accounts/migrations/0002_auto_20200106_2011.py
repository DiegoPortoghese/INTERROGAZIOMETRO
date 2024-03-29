# Generated by Django 3.0.1 on 2020-01-06 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classi', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePreferenzeMateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valore', models.IntegerField(default=0)),
                ('materia', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ProfiloPreferenzaMateria', to='classi.ClasseMateria', verbose_name='Materia')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='materie_preferite',
            field=models.ManyToManyField(blank=True, to='accounts.ProfilePreferenzeMateria', verbose_name='Materie preferite'),
        ),
    ]
