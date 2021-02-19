from django.contrib import admin
from .models import form2, formsApp
from django.utils.html import format_html
# Register your models here.
admin.site.register(form2)

@admin.register(formsApp)
class model1Admin(admin.ModelAdmin):
    def image_tag(self,obj):
        return format_html("<img src='{}' />".format(obj.imgesAdd.url))
    image_tag.short_description = 'Image'
    readonly_fields = ['image_tag']
# readonly_fields = ['image_tag','imgesAdd']
