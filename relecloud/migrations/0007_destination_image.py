# Generated by Django 5.0.6 on 2024-07-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0006_opinion'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='image',
            field=models.ImageField(default='images/imagenDefault.jpg', upload_to='images/'),
        ),
    ]
