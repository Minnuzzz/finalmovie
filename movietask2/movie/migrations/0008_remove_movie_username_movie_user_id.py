# Generated by Django 5.0.2 on 2024-03-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_movie_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='username',
        ),
        migrations.AddField(
            model_name='movie',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]