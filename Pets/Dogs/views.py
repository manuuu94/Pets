from django.shortcuts import render
import requests
from Dogs import models
# Create your views here.


def DogsMenu(request):
    try:


        return render(request,'dog-menu.html')
    except Exception as e:
        print(e)



def DogFind(request):
    try:
        dict = {}
        dict["lifespan"] = Lifespan()
        dict["temperament"] = Temperament()
        dict["trainability"] = Trainability()
        dict["size"] = Size()
        dict["hair"] = Hair()
        dict["color"] = Color()

        if request.method == "POST":
            lifespan = request.POST.get('lifespan')
            temperament = request.POST.get('temperament')
            trainability = request.POST.get('train')
            size = request.POST.get('size')
            hair = request.POST.get('hair')
            color = request.POST.get('color')

            print(f"{lifespan}-{temperament}-{trainability}-{size}-{hair}-{color}")
        

        return render(request,'dog-find.html', context=dict)
    except Exception as e:
        print(e)



def Lifespan():
    try:
        dict = {}
        lifespans = models.Lifespan.objects.all()
        index = 0
        for lifespan in lifespans:
            dict[index] = {"id":lifespan.id,"lifespan":lifespan.lifespan}
            index = index+1
        return dict
    except Exception as e:
        print(e)


def Temperament():
    try:
        dict = {}
        temperaments = models.Temperament.objects.all()
        index = 0
        for temp in temperaments:
            dict[index] = {"id":temp.id,"temperament":temp.temperament}
            index = index+1
        return dict 
    except Exception as e:
        print(e)

def Trainability():
    try:
        dict = {}
        trainability = models.Trainability.objects.all()
        index = 0
        for train in trainability:
            dict[index] = {"id":train.id,"trainability":train.trainability}
            index = index+1
        return dict
    except Exception as e:
        print(e)


def Size():
    try:
        dict = {}
        sizes = models.Size.objects.all()
        index = 0
        for size in sizes:
            dict[index] = {"id":size.id,"size":size.size}
            index = index+1
        return dict
    except Exception as e:
        print(e)

def Hair():
    try:
        dict = {}
        hairs = models.Hair.objects.all()
        index = 0
        for hair in hairs:
            dict[index] = {"id":hair.id,"hair":hair.hair}
            index = index+1
        return dict
    except Exception as e:
        print(e)

def Color():
    try:
        dict = {}
        colors = models.Color.objects.all()
        index = 0
        for color in colors:
            dict[index] = {"id":color.id,"color":color.color}
            index = index+1
        return dict
    except Exception as e:
        print(e)
