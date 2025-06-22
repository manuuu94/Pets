from django.shortcuts import render 



def Pets(request):
    try: 

        
        return render(request,'petshome.html')
    
    except Exception as e:
        print(e)