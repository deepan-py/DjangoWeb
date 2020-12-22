from django.contrib import admin
from .models import formsApp
# Register your models here.
admin.site.register(formsApp)


fields = ('image_tag')
readonly_fields = ('image_tag')
