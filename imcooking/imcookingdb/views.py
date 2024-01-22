from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Recipe, Ingredient, Step
from .forms import RecipeForm, IngredientFormSet, StepFormSet
from django.http import FileResponse
from django.db.models import Q
from django.db.models import Prefetch

from django.http import HttpResponse
from django.shortcuts import render
from urllib import request, parse
import http.client
import json
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


def example_request_view(ingredients):
    
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers = {
        
        'x-app-id': '0c2f5d87',
        'x-app-key': '307bf80eaa5e0e027e72580d58ac62ad',
    }
    queryText=''




    counter=0
    for ing in ingredients:
        if(counter==0):
            queryText=str(ing.Amount)+' '+ing.type.TypeName+' '+ing.name
        else:
            queryText=queryText+', '+str(ing.Amount)+' '+ing.type.TypeName+' '+ing.name
        counter=counter+1
    payload = {
        'query': queryText,
        "timezone": "Europe/Istanbul",
        "line_delimited": False,
        "use_raw_foods": False
    }
    json_data = json.dumps(payload)
    print(queryText)
    sums = {}

    if queryText!="":
        connection = http.client.HTTPSConnection('trackapi.nutritionix.com')
        connection.request('POST', url, body=json_data, headers=headers)
        response = connection.getresponse()
        if(response.status>=200  and response.status<300):
            content = response.read()
            connection.close()


            # Initialize a dictionary to store the sums for each case

            resultArry=[]
            print(content.decode('utf-8'))
            types=['cal','g','g','mg','mg','g','g','g','g','mg','mg']

            # Iterate through each element in the array
            for item in StringToDictinory(content.decode('utf-8')):
                # Split the element using ":"
                parts = item.split(":")

                # Extract the case and value
                case = parts[0]
                value = float(parts[1])

                # Add the value to the sum for the corresponding case
                if case in sums:
                    sums[case] += value
                else:
                    sums[case] = value

            # Print the sums for each casecount()
            count=0
            for case, total in sums.items():


                sums[case+"("+types[count]+")"] = sums.pop(case)
                count=count+1
                resultArry.append(str(case)+':'+str(total))
                print(f"{case}: {total}")


            return sums.items()
        else:
            return [f"HTTP Error {response.status}: {response.reason}"]
    else:
        return sums.items()



    # data_encoded = parse.urlencode(payload).encode('utf-8')
    # req = request.Request(url, data=data_encoded, headers=headers, method='POST')
    # try:
    #     print(req.get_full_url()+"        ------------------+++")
    #     with request.urlopen(req) as response:
    #     # Check if the request was successful (HTTP status code 2xx)
            
    #         if 200 <= response.status < 300:
    #            # Read and print the response content
    #            response_data = response.read().decode('utf-8')
    #            return StringToDictinory(response_data)
              
    #         else:
    #             return [f"HTTP Error {response.status}: {response.reason}"]
    # except request.HTTPError as e:
    #     return [f"HTTP Error {e.code}: {e.reason}"]
    # except request.URLError as e:
    #     return ["URL Error: {e.reason}"]


def StringToDictinory(text):
    textarray=text.split(',')
    resultList=[]
    filteredtextarray=list(filter(lambda k: 'nf' in k, textarray))
    for txt in filteredtextarray:
        resultList.append(txt.replace("nf_","").replace("\"",""))
    return resultList



def RecipeTitle(request, pk):
    recipe = get_object_or_404(Recipe, RecipeId=pk)
    print("-----------------")
    print(recipe.ingredients.all())
    if recipe.ingredients:
        print("xxxxxx               xxXxxxxXXxX")
        result=example_request_view(recipe.ingredients.all())
    print("ccccccccccc")
    print(result)
    
    return render(request, 'imcookingdb/RecipeTitle.html', {'recipe': recipe,'ings':result})

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

