from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Offer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name='offers')
    description = models.TextField(max_length=1000, verbose_name="Описание")
    job_title = models.CharField(max_length=50, verbose_name="Должность")
    is_active = models.BooleanField(default=True, null=False)
    is_employer = models.BooleanField(default=False, null=False)
    salary = models.IntegerField(verbose_name="Зарплата")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}: {self.job_title}, {self.salary} $\n{self.description[:50]}..."

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"


class EmployeerResume(models.Model):
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='employeer_resume')
    organization_name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='images/%Y', default='default_profile_photo.png')
    email = models.EmailField()
    phone_validator = RegexValidator(regex=r'^(?:\+7|8)\d{10}$')
    phone_number = models.CharField(validators=[phone_validator], max_length=12)
    date = models.DateField(auto_now_add=True)


class WorkerResume(models.Model):
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='worker_resume')
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    education = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    profile_photo = models.ImageField(default='default_profile_photo.png', upload_to='images/%Y')
    portfolio = models.FileField(upload_to='files/%Y')
    email = models.EmailField()
    phone_validator = RegexValidator(regex=r'^(?:\+7|8)\d{10}$')
    phone_number = models.CharField(validators=[phone_validator], max_length=12)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Message(models.Model):
    text = models.TextField(max_length=500)
    image = models.ImageField(upload_to='chat_images/%Y')
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='send_messages')
    receiver = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='receive_messages')
    time = models.TimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)