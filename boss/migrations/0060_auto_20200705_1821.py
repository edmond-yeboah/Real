# Generated by Django 3.0.6 on 2020-07-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0059_auto_20200705_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='departments',
        ),
        migrations.AlterField(
            model_name='region',
            name='hospitals',
            field=models.ManyToManyField(blank=True, to='boss.Hospital'),
        ),
        migrations.DeleteModel(
            name='departments',
        ),
    ]