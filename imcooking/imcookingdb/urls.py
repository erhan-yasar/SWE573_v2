from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('image/<str:name>', views.send_file, name='image'),
    path('post/<int:pk>/', views.RecipeTitle, name='RecipeTitle'),
    # path('post/new/', views.add_recipe, name='add_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe_photos/<str:name>', views.send_file, name='image')
]