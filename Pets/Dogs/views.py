from django.shortcuts import render
import requests

# Create your views here.


def DogsMenu(request):
    try:


        return render(request,'dog-menu.html')
    except Exception as e:
        print(e)



def DogFind(request):
    try:
        

        

        return render(request,'dog-find.html')
    except Exception as e:
        print(e)