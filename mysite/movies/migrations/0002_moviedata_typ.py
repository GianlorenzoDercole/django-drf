# Generated by Django 4.0.6 on 2023-01-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
