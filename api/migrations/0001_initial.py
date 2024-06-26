# Generated by Django 3.2 on 2021-06-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ammountinhand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Closedown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('costumername', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Closeup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('costumername', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Collectionlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('costumer_id', models.IntegerField(default=0)),
                ('costumer_name', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Costumerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('loanammount', models.IntegerField()),
                ('loan_date', models.CharField(max_length=300)),
                ('loanInterst', models.IntegerField()),
                ('ms', models.IntegerField()),
                ('place', models.CharField(max_length=300)),
                ('ammount_Balance', models.CharField(max_length=300)),
                ('place_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dlammounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Expence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('expenceName', models.CharField(max_length=300)),
                ('expenceAmmount', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Expencetotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inversment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Otherammountin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('reason', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Otherammountout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('reason', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=300)),
                ('reason', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
            ],
        ),
    ]
