from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
   UserId=models.AutoField(primary_key=True)
   UserName= models.CharField(max_length=100)
   UserEmail= models.CharField(max_length=100)
   UserEmail2= models.CharField(max_length=100)


class Recipe(models.Model):
    RecipeId=models.AutoField(primary_key=True)
    RecipeTitle= models.CharField(max_length=100)
    published_date= models.DateTimeField(default=timezone.now)
    RecipePhoto= models.CharField(max_length=100)
    RecipeIngredients= models.CharField(max_length=300)
    RecipeSteppes= models.CharField(max_length=300)



    




    
    