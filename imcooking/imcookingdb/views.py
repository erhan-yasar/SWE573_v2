from django.shortcuts import render
from django.utils import timezone
from .models import Recipe
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    posts = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    


    for x in posts:
        print(x.RecipeTitle)

    
    return render(request, 'imcookingdb/post_list.html', {'posts':posts })


def RecipeTitle(request, pk):
    recipes = get_object_or_404(Recipe, RecipeId=pk)
    print("-----------------")
    print(recipes.RecipeTitle)
    return render(request, 'imcookingdb/RecipeTitle.html', {'recipes': recipes})

def add_recipe(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            Recipe.published_date = timezone.now()
            Recipe.save(post)
            return redirect('RecipeTitle', pk=post.RecipeId)
    else:
        form = PostForm()
    return render(request, 'imcookingdb/add_recipe.html', {'form': form})