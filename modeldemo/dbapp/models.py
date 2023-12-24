from django.db import models

# Create your models here.
class employes(models.Model):
    empno=models.IntegerField()
    emoname=models.CharField(max_length=20)
    empaddres=models.CharField(max_length=100)
    empsalary=models.IntegerField()

def __str__(self):
    return "The employe details"+emoname