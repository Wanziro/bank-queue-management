# Generated by Django 4.0.6 on 2022-08-18 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_branches_address_branches_lat_branches_long_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_full_name', models.CharField(max_length=500)),
                ('email_address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 19, 36, 48, 244225))),
            ],
        ),
        migrations.AlterField(
            model_name='branches',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 19, 36, 48, 244225)),
        ),
    ]