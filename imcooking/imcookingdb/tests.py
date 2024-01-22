from django.test import TestCase
from django.urls import reverse
from .models import Recipe,Ingredient,IngredientTypes
from .views import example_request_view


# from .forms import RecipeForm, IngredientFormSet, StepFormSet

class TestViewsCase(TestCase):

    def setUp(self):
        self.recipe = Recipe.objects.create(RecipeTitle="Test Recipe",RecipePhoto="abcxyz")

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.RecipeTitle)

    def test_recipe_title_view(self):
        response = self.client.get(reverse('RecipeTitle', args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.RecipeTitle)   

# class TestFormsCase(TestCase):
#     def test_recipe_form_valid_data(self):
#         form_data = {'RecipeTitle': 'Test Recipe', 'PrepTime': 30, 'CookTime': 45, 'Rating': 4.5}
#         form = RecipeForm(data=form_data)
#         self.assertTrue(form.is_valid())

#     def test_ingredient_formset_valid_data(self):
#         form_data = {'ingredients-TOTAL_FORMS': 1, 'ingredients-INITIAL_FORMS': 0,
#                      'ingredients-MIN_NUM_FORMS': 0, 'ingredients-MAX_NUM_FORMS': 1000,
#                      'ingredients-0-name': 'Carrot', 'ingredients-0-type': 1, 'ingredients-0-Amount': 100}
#         formset = IngredientFormSet(data=form_data, prefix='ingredients')
#         self.assertTrue(formset.is_valid())

#     def test_step_formset_valid_data(self):
#         form_data = {'steps-TOTAL_FORMS': 1, 'steps-INITIAL_FORMS': 0,
#                      'steps-MIN_NUM_FORMS': 0, 'steps-MAX_NUM_FORMS': 1000,
#                      'steps-0-description': 'Chop the vegetables'}
#         formset = StepFormSet(data=form_data, prefix='steps')
#         self.assertTrue(formset.is_valid())
        


class TestAPICase(TestCase):
   

    def test_api(self):
        test1=Ingredient()
        test1.name="garlic powder"
        test1.Amount=1.0
        test1.type=IngredientTypes()
        test1.type.TypeName="tablespoon"
        result={
        "calories(cal)":31.44,
        "total_fat(g)":0.07,
        "saturated_fat(g)":0.02,
        "cholesterol(mg)":0.0,
        "sodium(mg)":5.7,
        "total_carbohydrate(g)":6.91,
        "dietary_fiber(g)":0.86,
        "sugars(g)":0.23,
        "protein(g)":1.57,
        "potassium(mg)":113.33,
        "p(mg)":39.33
        }
        test=[]
        test.append(test1)
        
        self.assertEqual(example_request_view(test),result.items())


        
        