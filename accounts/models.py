from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    about = models.CharField(max_length=300, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='picture', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
  
    def __str__(self) -> str:
        return self.user.username