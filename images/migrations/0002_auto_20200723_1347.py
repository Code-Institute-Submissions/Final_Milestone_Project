# Generated by Django 3.0.8 on 2020-07-23 13:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.AlterModelOptions(
            name='image_data',
            options={'verbose_name_plural': 'Image_Data'},
        ),
    ]
