# Generated by Django 4.1.4 on 2022-12-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='gia',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='sanpham',
            name='hinhanh',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]