# Generated by Django 3.0.1 on 2020-01-02 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('displayed', models.BooleanField(default=False, verbose_name='Visualizzato')),
                ('from_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message_from', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
