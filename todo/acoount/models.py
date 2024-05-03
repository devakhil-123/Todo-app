from django.db import models

# Create your models here.

class todoModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date=models.DateField(null=True)
    image=models.ImageField(upload_to="todoimages")