# Generated by Django 2.1.7 on 2019-04-15 23:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fenster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fenster',
            name='fenster_height',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='fenster',
            name='fenster_scheme',
            field=models.CharField(default='1,2', max_length=1024, validators=[django.core.validators.int_list_validator]),
        ),
        migrations.AlterField(
            model_name='fenster',
            name='fenster_width',
            field=models.IntegerField(default=50),
        ),
    ]
