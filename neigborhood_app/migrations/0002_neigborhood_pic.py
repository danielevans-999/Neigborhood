# Generated by Django 2.2.7 on 2019-12-02 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neigborhood_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neigborhood',
            name='pic',
            field=models.ImageField(default='media/hoods/lagoon.jpg', upload_to='hoods/'),
        ),
    ]
