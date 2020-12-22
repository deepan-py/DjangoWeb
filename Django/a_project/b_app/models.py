from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.

class Topic(models.Model):
    top_name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage, on_delete=DO_NOTHING)
    date=models.DateField()

    def __str__(self):
        return str(self.date)
