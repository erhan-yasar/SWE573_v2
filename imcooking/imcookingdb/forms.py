from django import forms
from django.forms.models import BaseModelFormSet

from .models import Recipe, Ingredient, Step

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Recipe
#         fields = ('RecipeId','RecipeTitle', 'RecipeIngredients','RecipeSteppes')

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['RecipeTitle', 'RecipePhoto','PrepTime','CookTime']



IngredientFormSet = forms.inlineformset_factory(
    Recipe, Ingredient, fields=('name',), widgets={
        
        'name':forms.TextInput(attrs={'size': '45',})
    }, extra=9, min_num=1, validate_min=False
)

StepFormSet = forms.inlineformset_factory(
    Recipe, Step, fields=('description',), widgets={
         
        'description':forms.TextInput(attrs={'size': '100',}), 
    },
    
    extra=9, min_num=1, validate_min=False
)