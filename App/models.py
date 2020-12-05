from django.db import models
from django.contrib.auth.models import User
from .storage import OverwriteStorage
from datetime import datetime    

class users(models.Model):  
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    User_Name = models.CharField(max_length=20) 
    Email = models.CharField(max_length=40) 
    Password  = models.CharField(max_length=20)  
      
    def __str__(self):
        return self.User_Name 

class DiabTest(models.Model):
    user = models.CharField(max_length=50,null=True)
    Pregnancies=models.FloatField(default=0)
    Glucose=models.FloatField(default=0)
    BP=models.IntegerField(default=0)
    Skinthickness=models.FloatField(default=0)
    Insulin=models.FloatField(default=0)
    BMI=models.FloatField(default=0)
    Diabetic_pf=models.FloatField(default=0)
    age=models.FloatField(default=10)
    Res=models.CharField(max_length=10,null=True)
    Testdate = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return str(self.user)

class HeartTest(models.Model):
    user = models.CharField(max_length=50,null=True)
    age=models.FloatField(default=0)
    anaemia=models.FloatField(default=0)
    creatinine_phosphokinase=models.IntegerField(default=0)
    diabetes=models.FloatField(default=0)
    ejection_fraction=models.FloatField(default=0)
    high_blood_pressure=models.FloatField(default=0)
    platelets=models.FloatField(default=0)
    serum_creatinine=models.FloatField(default=10)
    serum_sodium=models.FloatField(max_length=10,null=True) 
    sex=models.FloatField(max_length=10,null=True) 
    smoking=models.FloatField(max_length=10,null=True) 
    time=models.FloatField(max_length=10,null=True) 
    DEATH_EVENT=models.CharField(max_length=10,null=True) 
    Testdate = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return str(self.user)

class Med_file(models.Model):
    filename = models.CharField(max_length=200)
    mediafile = models.FileField(storage=OverwriteStorage())

    def __str__(self):
        return self.filename										        