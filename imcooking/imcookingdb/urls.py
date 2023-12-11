from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.RecipeTitle, name='RecipeTitle'),
    path('post/new/', views.add_recipe, name='add_recipe')
]