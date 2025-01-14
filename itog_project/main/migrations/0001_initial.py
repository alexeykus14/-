# Generated by Django 4.2.6 on 2023-10-23 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('job_title', models.CharField(max_length=50, verbose_name='Должность')),
                ('is_active', models.BooleanField(default=True)),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('portfolio', models.FileField(upload_to='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Обьявление',
                'verbose_name_plural': 'Обьявления',
            },
        ),
    ]
