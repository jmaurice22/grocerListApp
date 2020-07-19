
from django.shortcuts import render
from .models import Fruits
from django.http import HttpResponseRedirect

# Create your views here.

def fruits_list_view(request):
    fruit = Fruits.objects.all()

    content = {
        'fruits': fruit
    }
    
    return render(request, "website/home.html", content)
            
            
            

def addItem(request):

    new_item = Fruits(name = request.POST['name'])
    new_item.save()
    return HttpResponseRedirect('')
    # Create a new item
    #save
    #redirect browser




