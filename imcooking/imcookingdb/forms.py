from django import forms
from django.forms.models import BaseModelFormSet

from .models import Recipe, Ingredient, Step,IngredientTypes

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Recipe
#         fields = ('RecipeId','RecipeTitle', 'RecipeIngredients','RecipeSteppes')

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['RecipeTitle', 'RecipePhoto','PrepTime','CookTime']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'Amount', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the 'type' field to be a dropdown with choices from IngredientTypes
        self.fields['type'].queryset = IngredientTypes.objects.all()

    def __str__(self):
        return f"{self.instance.TypeId}: {self.instance.TypeName}"


IngredientFormSet = forms.inlineformset_factory(
    Recipe, Ingredient,  fields=('name','Amount','type'), widgets={
        
        'name':forms.TextInput(attrs={'size': '30',}),
        'Amount':forms.NumberInput(attrs={'size': '9',}),
        'type':forms.Select(attrs={'size': '1',})
    }, extra=19, min_num=1, validate_min=False
)

StepFormSet = forms.inlineformset_factory(
    Recipe, Step, fields=('description',), widgets={
         
        'description':forms.TextInput(attrs={'size': '100',}), 
    },
    
    extra=19, min_num=1, validate_min=False
)