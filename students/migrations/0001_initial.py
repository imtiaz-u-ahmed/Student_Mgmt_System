# Generated by Django 2.1.1 on 2018-10-11 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll', models.IntegerField()),
                ('std_class', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
