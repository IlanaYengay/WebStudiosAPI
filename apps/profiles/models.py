from datetime import date
from django.db import models
from apps.accounts.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    birthdate = models.DateField()

    @property
    def age(self):
        today = date.today()

        return today.year - self.birthdate.year - (
                (today.month, today.day) < (self.birthdate.month, self.birthdate.day))



    def __str__(self):
        return str(self.id)