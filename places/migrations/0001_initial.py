# Generated by Django 3.2 on 2022-02-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.IntegerField()),
                ('place', models.CharField(max_length=300)),
            ],
        ),
    ]
