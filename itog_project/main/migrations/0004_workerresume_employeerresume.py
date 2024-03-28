# Generated by Django 4.2.6 on 2023-10-30 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_remove_offer_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('profile_photo', models.ImageField(default='default_profile_photo.png', upload_to='media/%Y')),
                ('portfolio', models.FileField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeerResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100)),
                ('profile_photo', models.ImageField(default='default_profile_photo.png', upload_to='media/%Y')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
