# Generated by Django 3.1.7 on 2021-04-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='img',
            field=models.ImageField(default='huvwai', upload_to='images'),
            preserve_default=False,
        ),
    ]