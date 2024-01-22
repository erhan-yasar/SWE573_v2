from django.test import TestCase
from django.urls import reverse
from .models import Recipe

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