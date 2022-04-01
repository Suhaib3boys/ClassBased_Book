from pyexpat import model
from django.db import models

# Create your models here.
class Books(models.Model):
    Book_name = models.CharField(max_length=70)
    Publish_year = models.IntegerField()
    Image = models.ImageField(upload_to='IMG')
    Book_description = models.TextField(max_length=350)
    Writer = models.CharField(max_length=70)

    def __str__(self):
        return self.Book_name