from django.db import models
from django.utils.html import mark_safe, escape
# from django import forms
# Create your models here.
gender_choices = (
    ('M','Male'),
    ('F','Female'),
)

multichoice = (
    ('1','one'),
    ('2','two'),
    ('3','three')
)

class formsApp(models.Model):
    first_name = models.CharField(max_length=256,blank=True,default='00000')
    last_name = models.CharField(max_length=256)
    email_Id = models.EmailField(max_length=512,unique=True)
    phone_number = models.IntegerField(default=5)
    DateOfEntry = models.DateField(auto_now_add=True)
    DateOfBirth = models.DateField(null=True)
    DateTimeOfEntry = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=1,choices=gender_choices)
    gender_radio = models.CharField(choices=gender_choices, max_length=1,default='M')
    imgesAdd = models.ImageField(upload_to = 'media/images/',blank=True,null=True)
    filesUpload = models.FileField(upload_to='templates/files',blank=True)
