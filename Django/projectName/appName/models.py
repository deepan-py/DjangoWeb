from django.db import models

# Create your models here.

class countries(models.Model):
    name = models.CharField(max_length=200,blank=False,default='')
    capital = models.CharField(max_length=256,blank=False,default='')

    class Meta:
        ordering = ('id',)