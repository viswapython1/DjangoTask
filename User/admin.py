from django.contrib import admin
from .models import User,Post
class AdminUser(admin.ModelAdmin):
    list_display=['first_name','last_name','email','password','username']
class AdminPost(admin.ModelAdmin):
    list_display = ['user','text','created_at','updated_at']

# Register your models here.
admin.site.register(User,AdminUser)
admin.site.register(Post,AdminPost)
