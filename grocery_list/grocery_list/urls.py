"""grocery_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.fruits, name='fruits')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='fruits')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from fruits.views import fruits_list_view, updateItem, deleteItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fruits_list_view,),
    path('home/', fruits_list_view ),
    path('updateItem/<str:pk>/', updateItem, name="Update Item"),
    path('deleteItem/<str:pk>/', deleteItem, name="delete"),

]
