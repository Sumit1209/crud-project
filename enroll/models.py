from django.db import models

# Create your models here.


class Student(models.Model):
    student_name=models.CharField(max_length=100,null=False)
    dep= models.CharField(max_length=100)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.CharField(max_length=100)
    phone=models.IntegerField()
    hire_date=models.DateTimeField()
