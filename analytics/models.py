from django.db import models
from django.contrib.auth.models import User

class PageView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)