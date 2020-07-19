
from django.shortcuts import render, redirect

from .forms import ItemForm
from .models import Fruits
from django.http import HttpResponseRedirect

# Create your views here.

def fruits_list_view(request):
    fruit = Fruits.objects.all()

    form = ItemForm()

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
                form.save()
        return redirect('/')


    content = {
        'fruits': fruit, 'form': form,
    }
    
    return render(request, "website/home.html", content)
            
            
            

def updateItem(request, pk):

    item = Fruits.objects.get(id=pk)

    form = ItemForm(instance=item)

    if request.method == 'POST':
        form = ItemForm(request.Post, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    content = {
         'form': form,
    }
    return render(request, 'website/updateItem.html', content)


def deleteItem(request, pk):
    item = Fruits.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    content = {
        'item': item,
    }
    return render(request, 'website/deleteItem.html', content)




