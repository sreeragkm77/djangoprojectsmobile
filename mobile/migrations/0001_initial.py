# Generated by Django 3.1.7 on 2021-04-11 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('model_name', models.CharField(max_length=80)),
                ('specs', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=120)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.brands')),
            ],
        ),
    ]
