# Generated by Django 2.2 on 2021-11-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Mobile', models.BigIntegerField()),
                ('Start_date', models.DateTimeField()),
                ('Salary', models.FloatField()),
                ('Employee_ID', models.CharField(max_length=6)),
            ],
        ),
    ]
