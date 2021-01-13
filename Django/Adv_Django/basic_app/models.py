from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100,unique=True)
    principal = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # the below code is used to redirect it to the detail that is scl_details.html which show the detail of the current school that we created
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={"pk": self.pk})
    

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.DO_NOTHING)
    # the on_delete=models.CASCADE will delete the entry as well as its associate values
    # the on_delete=models.DO_NOTHING while deleting value if it has foreign key value in another table it cause FOREIGN_KEY error
    # on_delete=None will cause NoneType error 

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={"pk": self.pk})
    