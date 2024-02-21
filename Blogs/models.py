from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    teacher = models.CharField(max_length=100)
    age = models.IntegerField(max_length=5)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)


    






    def __str__(self):
        return f" Your name is {self.teacher}"