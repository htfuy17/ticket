from django.db import models

class Exhibition(models.Model):
    photo = models.CharField(max_length=10, unique=True)
    news = models.CharField(max_length=10, unique=True)

class Meta:
        unique_together = ('photo','news')
        
def __str__(self):
    return self.news