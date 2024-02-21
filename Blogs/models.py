from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    teacher = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return f"{self.teacher}"



class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE) 

    def __str__(self):
        return f" {self.name}"






















  