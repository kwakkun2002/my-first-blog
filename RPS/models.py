from django.db import models

# Create your models here.

class Input(models.Model):
    RPS_oneOfThree = models.CharField(max_length=10)
    
    

class Data(models.Model):
    whatPlayerDo = models.CharField(max_length=10)
    battle_status = models.IntegerField()
    num = models.IntegerField()
    
    








