# Generated by Django 2.1.1 on 2018-10-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuardianInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=20)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]