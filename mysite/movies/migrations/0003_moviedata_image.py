# Generated by Django 4.0.6 on 2023-01-26 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
