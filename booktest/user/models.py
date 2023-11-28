from django.db import models
from celery_app import send_mail


class UserBook(models.Model):
    username = models.CharField(max_length=60)
    mail = models.EmailField(max_length=70)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        send_mail.delay(self.username, self.mail)

        return super().save(*args, **kwargs)

