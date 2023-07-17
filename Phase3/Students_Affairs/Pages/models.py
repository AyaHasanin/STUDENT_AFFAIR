#from asyncio.windows_events import NULL
from django.db import models
# Create your models here.
class Members(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=255)
    department=models.CharField(max_length=10)
    level=models.IntegerField()
    gender=models.CharField(max_length=7)
    email=models.EmailField(max_length=100)
    gpa=models.DecimalField(max_digits=8,decimal_places=2)
    phone=models.IntegerField()
    status=models.CharField(max_length=10)
    birth=models.DateField(null=True)