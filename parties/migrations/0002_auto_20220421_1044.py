# Generated by Django 3.2 on 2022-04-21 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parties',
            name='ammount_Balance',
        ),
        migrations.AddField(
            model_name='parties',
            name='email_id',
            field=models.CharField(default='none', max_length=300),
        ),
    ]
