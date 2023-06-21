from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    target = models.CharField(max_length=255, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)


# models.py
from .telegram_utils import send_telegram_message

class TrainingRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_type = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=20)
    time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.training_type} ({self.day_of_week}, {self.time})"
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Отправка сообщения в Telegram
        chat_id = '657099124'
        message = f'Новая запись на тренеровку от ({self.user.username}). На странице расписания. Запись на ({self.training_type}). День недели: {self.day_of_week}. Время: {self.time}'
        send_telegram_message(chat_id, message)
