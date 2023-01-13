from django.db import models
from django.core.validators import RegexValidator


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'