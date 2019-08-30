from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher= models.CharField(max_length=50)
    publication_year = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

