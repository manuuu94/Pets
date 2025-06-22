

from django.urls import path
from . import views

urlpatterns = [
    path('dog-menu/',views.DogsMenu,name='dog-menu'),
    path('dog-find',views.DogFind,name='dog-find'),


]



