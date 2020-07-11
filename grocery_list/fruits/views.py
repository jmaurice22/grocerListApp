
from django.shortcuts import render
from .models import Fruits

# Create your views here.

def fruits_list_view(request):
    fruit = Fruits.objects.all()
    context = {
        'fruit': fruit
    }
    return render(request, "website/fruits.html", context)


