# Generated by Django 4.2.6 on 2023-10-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_offer_is_employer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='portfolio',
        ),
    ]
