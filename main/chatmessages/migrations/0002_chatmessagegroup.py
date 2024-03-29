# Generated by Django 3.0.1 on 2020-01-06 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classi', '0001_initial'),
        ('chatmessages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessageGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='group_message_from', to=settings.AUTH_USER_MODEL)),
                ('group_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='group_chat', to='classi.Classe')),
            ],
        ),
    ]
