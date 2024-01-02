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
    RecipePhoto= models.ImageField(upload_to='recipe_photos/')
    PrepTime = models.IntegerField(null=True)
    CookTime = models.IntegerField(null=True)
    Rating = models.FloatField(null=True)

class Ingredient(models.Model):
     recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
     name = models.CharField(max_length=300)
     TypeId = models.IntegerField(null=True)
     Amount = models.FloatField(null=True)

class Step(models.Model):
    StepOrder = models.IntegerField(null=True)
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

# class IngredientTypes(models.Model):
#      Ingredient = models.ForeignKey(Ingredient, related_name='IngredientType', on_delete=models.CASCADE)
#      TypeId=models.AutoField(primary_key=True)
#      TypeName = models.CharField(max_length=50)

# class IngredientTypes(models.Model):
#     TypeId = models.AutoField(primary_key=True)
#     TypeName = models.CharField(max_length=50)

# class Ingredient(models.Model):
#     recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
#     name = models.CharField(max_length=300, null=True)
#     type = models.ForeignKey(IngredientTypes, on_delete=models.CASCADE)
#     Amount = models.FloatField(null=True)

    




    
    