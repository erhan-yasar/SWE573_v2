from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Recipe, Ingredient, Step
from .forms import RecipeForm, IngredientFormSet, StepFormSet
from django.http import FileResponse
from django.db.models import Q
from django.db.models import Prefetch
import itertools





    



# Create your views here.

def post_list(request):
    query = request.GET.get('q')
    if query :
       posts = Recipe.objects.filter(Q(RecipeTitle__icontains=query) )
        # if query=='' and queryI:
        #     posts = Recipe.objects.filter(published_date__lte=timezone.now()).prefetch_related(Prefetch("ingredients",queryset=Ingredient.objects.filter(name=queryI),to_attr="filtered_ingredients"))
        #& Recipe.objects.filter(published_date__lte=timezone.now())
    else:
        posts = Recipe.objects.filter(published_date__lte=timezone.now())
    posts=posts.order_by('-published_date')
    for x in posts:
        if (x.RecipePhoto):
            result=x.RecipePhoto=x.RecipePhoto.url.split('/')
            if(len(result)>2):
                x.RecipePhoto=result[2]
    return render(request, 'imcookingdb/post_list.html', {'posts':posts })

def filtering_function(obj):
    return any(x.name == "t2" for x in obj)
    


def send_file(response,name):
    
    img = open('recipe_photos\\' + name, 'rb')

    response = FileResponse(img)

    return response



def RecipeTitle(request, pk):
    recipe = get_object_or_404(Recipe, RecipeId=pk)
    print("-----------------")
    print(list(recipe.ingredients.all()))
    return render(request, 'imcookingdb/RecipeTitle.html', {'recipe': recipe})

# def add_recipe(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             Recipe.published_date = timezone.now()
#             Recipe.save(post)
#             return redirect('RecipeTitle', pk=post.RecipeId)
#     else:
#         form = PostForm()
#     return render(request, 'imcookingdb/add_recipe.html', {'form': form})

def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        ingredient_formset = IngredientFormSet(request.POST, prefix='ingredients')
        step_formset = StepFormSet(request.POST, prefix='steps')

        if recipe_form.is_valid() and ingredient_formset.is_valid() and step_formset.is_valid():
            recipe = recipe_form.save()

            for ingredient_form in ingredient_formset:
                if ingredient_form.cleaned_data.get('name'):
                    Ingredient.objects.create(recipe=recipe, name=ingredient_form.cleaned_data['name'],Amount=ingredient_form.cleaned_data['Amount'],type=ingredient_form.cleaned_data['type'])

            for step_form in step_formset:
                if step_form.cleaned_data.get('description'):
                    Step.objects.create(recipe=recipe, description=step_form.cleaned_data['description'])

            return redirect('RecipeTitle', pk=recipe.RecipeId)  # Redirect to a page indicating successful recipe addition
 
    else:
        recipe_form = RecipeForm()
        ingredient_formset = IngredientFormSet(prefix='ingredients')
        step_formset = StepFormSet(prefix='steps')

    return render(request, 'imcookingdb/add_recipe.html', {
        'recipe_form': recipe_form,
        'ingredient_formset': ingredient_formset,
        'step_formset': step_formset,
    })

