# Generated by Django 4.1.6 on 2023-04-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=100)),
            ],
        ),
    ]
