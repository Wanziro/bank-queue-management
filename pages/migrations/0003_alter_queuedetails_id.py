# Generated by Django 4.0.6 on 2022-08-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_jsondate_queuedetails_joinedtimeanddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queuedetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
