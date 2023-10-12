import string
import random
from django.db import models
from apps.accounts.models import CustomUser


def generate_order_number():
    return ''.join(random.choices(string.digits, k=6))

class Order(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_order')
    order_number = models.CharField(max_length=6, default=generate_order_number, unique=True)
    created_at = models.DateField(auto_now_add=True)
    # status = models.CharField(max_length=20, default='Новый')
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('in_process', 'В обработке'),
        # ('Завершен', 'Завершен'),
        # ('Отменен', 'Отменен'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    images = models.ManyToManyField('Image', blank=True)


    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = generate_order_number()
        super(Order, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.FileField(upload_to='images/')

    def __str__(self):
        return self.file.name


