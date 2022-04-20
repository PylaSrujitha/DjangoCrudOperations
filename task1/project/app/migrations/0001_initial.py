# Generated by Django 4.0.3 on 2022-04-09 06:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LasttName', models.CharField(max_length=200)),
                ('Username', models.CharField(max_length=200)),
                ('MobileNumber', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('branch', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'register_table',
            },
        ),
    ]