from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=10, unique=True)
    ticket = models.CharField(max_length=10, unique=True)
    number = models.CharField(max_length=10, unique=True)

class Meta:
        unique_together = ('name','phone','title','ticket','number')
        
def __str__(self):
    return self.title
