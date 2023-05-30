from django.db import models
from accounts.models import Account


class Post(models.Model):
    text = models.TextField()
    file = models.FileField(upload_to='file', null=True, blank=True)
    owner = models.ForeignKey(
        Account, 
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    