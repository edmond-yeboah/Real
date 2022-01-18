# Generated by Django 3.0.6 on 2020-07-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0058_auto_20200705_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='region',
            name='hospitals',
            field=models.ManyToManyField(blank=True, to='boss.Hospital'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='facility',
            field=models.ManyToManyField(blank=True, to='boss.facility'),
        ),
    ]