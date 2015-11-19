from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    num = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','name','num','major')
    
admin.site.register(User,UserAdmin)
