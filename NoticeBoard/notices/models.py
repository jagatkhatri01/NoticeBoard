from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class CRNotice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title