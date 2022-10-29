from django.db import models

# Create your models here.
class LoginPage(models.Model):
    user_name = models.CharField(max_length=264,unique=True)
    user_email= models.EmailField(max_length=264,unique=True)
    user_password=models.CharField(max_length=50)
    user_number= models.IntegerField()
    def __str__(self):
        return user_name
class Flight(models.Model):
    roundtrip= models.CharField(max_length=50)
    oneway= models.CharField(max_length=50)
    multiway= models.CharField(max_length=50)
    flying_from = models.CharField(max_length=50)
    flying_to = models.CharField(max_length=50)
    departing = models.CharField(max_length=50)
    returning = models.CharField(max_length=50)
    no_of_passengers= models.IntegerField()
    classes= models.CharField(max_length=50)
    def __str__(self):
        pass
        
