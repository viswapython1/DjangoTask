from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.TextField(default=None)
    last_name = models.TextField(default=None)
    email = models.EmailField(default=None)
    password = models.IntegerField(default=None)
    username = models.TextField(default=None)

    class Meta:
        db_table='User'

    def __str__(self):
        return self.first_name



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default=None)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=0)

    class Meta:
        db_table="Post"

    def __str__(self):
        return self.user

