# Generated by Django 3.0.8 on 2020-08-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0016_auto_20200820_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='prev_img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='tmnl_img',
            field=models.ImageField(upload_to=''),
        ),
    ]
