# Generated by Django 3.0.6 on 2020-07-02 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0017_auto_20200702_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='covid_about',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='pop_about',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]