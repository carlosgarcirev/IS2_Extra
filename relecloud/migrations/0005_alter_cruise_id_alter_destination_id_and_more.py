# Generated by Django 5.0.6 on 2024-07-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0004_auto_20210331_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cruise',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inforequest',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
