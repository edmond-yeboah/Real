# Generated by Django 3.0.6 on 2020-06-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0012_bank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(default='default.png', upload_to='')),
                ('population', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(default='default.png', upload_to='')),
                ('population', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(default='default.png', upload_to='')),
                ('population', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]