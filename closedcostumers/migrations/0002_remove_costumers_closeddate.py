# Generated by Django 3.2 on 2022-03-15 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('closedcostumers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costumers',
            name='closeddate',
        ),
    ]
