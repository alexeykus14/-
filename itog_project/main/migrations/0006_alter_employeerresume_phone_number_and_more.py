# Generated by Django 4.2.6 on 2023-11-03 16:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_workerresume_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeerresume',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='^(?:\\+7|8)\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='employeerresume',
            name='profile_photo',
            field=models.ImageField(default='media/default_profile_photo.png', upload_to='media/%Y'),
        ),
        migrations.AlterField(
            model_name='workerresume',
            name='portfolio',
            field=models.FileField(upload_to='files/%Y'),
        ),
        migrations.AlterField(
            model_name='workerresume',
            name='profile_photo',
            field=models.ImageField(default='media/default_profile_photo.png', upload_to='images/%Y'),
        ),
    ]