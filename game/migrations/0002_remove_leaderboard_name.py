# Generated by Django 3.2.7 on 2021-10-07 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='name',
        ),
    ]
