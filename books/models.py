from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(Author,related_name='books' , on_delete=models.CASCADE)
    owner = models.ForeignKey(User,null=True, related_name='books' , on_delete=models.SET_NULL)
    
