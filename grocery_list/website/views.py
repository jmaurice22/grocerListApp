
from django.shortcuts import render
from fruits.models import Fruits

# Create your views here.


#
def GroceryList(request):
    
    fruit = Fruits.objects.all()

    context = {
        'message':"Welcome to your grocery list!. Please add and remove items by selecting the options below.",
        'items': fruit
    }
    return render(request, "website/home.html", context)

