# Generated by Django 4.2.6 on 2023-11-07 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_alter_employeerresume_owner_alter_offer_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='chat_images/%Y')),
                ('time', models.TimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]