from django.db import models

# Create your models here.
class ContactW (models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name+" , "+self.email

class ContactP (models.Model):
    service=models.CharField(max_length=100)
    validity=models.CharField(max_length=100)
    data=models.CharField(max_length=100)
    plan=models.CharField(max_length=100)
    
    def __str__(self):
        return self.service+" , "+self.validity