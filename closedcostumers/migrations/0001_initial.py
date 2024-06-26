# Generated by Django 3.2 on 2022-03-15 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costumer_id', models.IntegerField()),
                ('costumer_name', models.CharField(max_length=300)),
                ('place', models.CharField(max_length=300)),
                ('loandate', models.CharField(max_length=300)),
                ('closeddate', models.DateTimeField(auto_now_add=True)),
                ('loanammount', models.IntegerField()),
                ('loanintrest', models.IntegerField()),
                ('ms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costumer_id', models.IntegerField()),
                ('costumer_name', models.CharField(max_length=300)),
                ('ammount', models.IntegerField()),
                ('date', models.CharField(max_length=300)),
            ],
        ),
    ]
