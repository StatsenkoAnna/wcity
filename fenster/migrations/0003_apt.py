# Generated by Django 2.1.7 on 2019-04-15 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fenster', '0002_auto_20190415_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('fenster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fenster.Fenster')),
            ],
        ),
    ]
