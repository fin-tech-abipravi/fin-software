# Generated by Django 3.2 on 2022-10-18 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_accessusers_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessusers',
            name='date',
            field=models.CharField(default=datetime.date(2022, 10, 18), max_length=300),
        ),
    ]
