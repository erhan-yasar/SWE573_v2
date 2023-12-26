from django import forms

from .models import Recipe, Ingredient, Step, IngredientTypes

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Recipe
#         fields = ('RecipeId','RecipeTitle', 'RecipeIngredients','RecipeSteppes')

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['RecipeTitle', 'RecipePhoto','PrepTime','CookTime']

Multiplier= (
    (1,0.25),
    (2,0.5),
    (3,0.75),
    (4,1),
    (5,1.25),
    (6,1.5),
    (7,1.75),
    (8,2),
)
IngredientFormSet = forms.inlineformset_factory(
    Recipe, Ingredient, fields=('name','Amount','TypeId') ,widgets={
        
        'TypeId':forms.Select(choices=Multiplier),
        'name':forms.TextInput(attrs={'size': '6',}),
        'Amount':forms.TextInput(attrs={'size': '4',}),
    }, extra=5, min_num=1, validate_min=True
)

StepFormSet = forms.inlineformset_factory(
    Recipe, Step, fields=('StepOrder','description',), extra=5, min_num=1, validate_min=True
)