from django.db import models
from django.contrib.auth.models import User

# Create your models here.s
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Options(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=None,null=True)
    question=models.CharField(max_length=100)
    option1=models.CharField(max_length=60)
    option2=models.CharField(max_length=60)
    option3=models.CharField(max_length=60)
    option4=models.CharField(max_length=60)
    answer=models.CharField(max_length=60)


    def __str__(self):
        return self.question



class Test(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.ForeignKey(Options, on_delete=models.CASCADE)
    answer=models.CharField(max_length=50)