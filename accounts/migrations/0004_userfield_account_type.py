# Generated by Django 3.2 on 2022-09-20 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220920_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfield',
            name='account_type',
            field=models.CharField(default='user', max_length=300),
        ),
    ]
