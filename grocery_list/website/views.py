
from django.shortcuts import render

# Create your views here.


#
def home(request):

    context = {
        'message':"Welcome to your grocery list!. Please add and remove items by selecting the options below."
    }
    return render(request, "website/home.html", context)

def fruits(request):
    
    return render(request, "website/fruits.html")