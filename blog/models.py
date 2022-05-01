from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from postgres_copy  import CopyManager
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(null=True)
    


    def __str__(self):
        return self.title
    

