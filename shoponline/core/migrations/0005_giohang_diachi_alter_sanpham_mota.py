# Generated by Django 4.1.4 on 2022-12-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_donhang_giohang_donhang_giohang_donhang_sanpham'),
    ]

    operations = [
        migrations.AddField(
            model_name='giohang',
            name='diachi',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='sanpham',
            name='mota',
            field=models.CharField(max_length=500),
        ),
    ]