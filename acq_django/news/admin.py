from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Album)
admin.site.register(models.Musician)
admin.site.register(models.Person)
admin.site.register(models.Group)
admin.site.register(models.Membership)
admin.site.register(models.MyFiles)
