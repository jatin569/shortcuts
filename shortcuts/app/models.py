from django.db import models

# Create your models here.
class signup(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    Phone = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)
class My_model(models.Model):
    title = models.CharField(max_length=25)
    pdf = models.FileField(upload_to='static/media')


    def __str__(self):
        return self.title