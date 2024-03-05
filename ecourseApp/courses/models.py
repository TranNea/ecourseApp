from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)


    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Courses(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m/')
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name