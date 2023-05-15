from email.policy import default
from django.db import models

# Create your models here.
class Projets(models.Model):
    id = models.IntegerField(primary_key = True)
    Nameproject = models.CharField(max_length=50 )
    Description = models.CharField(max_length = 500 , default='En cours')
    Photo = models.URLField()
    

class Formations(models.Model):
    id = models.IntegerField(primary_key = True)
    NameFormation = models.CharField(max_length=50 )
    F_Date = models.DateField()
    F_photo = models.URLField()
    F_Description = models.CharField(max_length = 500 , default='En cours')

class TeamBuilding(models.Model):
    id = models.IntegerField(primary_key = True)
    T_Name = models.CharField(max_length=50 )
    T_Date = models.DateField()
    T_photo = models.URLField()
    T_Description = models.CharField(max_length = 500 , default='En cours')

    
class Institue(models.Model):
    id = models.IntegerField(primary_key = True)
    I_Name = models.CharField(max_length=50 )
    I_Date = models.DateField()
    I_photo = models.URLField()
    I_Description = models.CharField(max_length = 500 , default='En cours')


class Event(models.Model):
    id = models.IntegerField(primary_key = True)
    E_Name = models.CharField(max_length=50 )
    E_Date = models.DateField()
    E_photo = models.URLField()
    E_Description = models.CharField(max_length = 500 , default='En cours')
    E_Day = models.IntegerField()
    E_Month = models.CharField(max_length=20 )
    E_Year = models.PositiveBigIntegerField( )


    

