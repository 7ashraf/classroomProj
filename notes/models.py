from django.db import models

# Create your models here.
class Notes(models.Model):
    noteTitle = models.CharField(max_length=100)
    noteContent = models.TextField()
    author = models.CharField(max_length = 100)

    def __str__(self):
        return f"Note Title: {self.noteTitle}"
