from django.db import models
from django.forms import ModelForm

# Create your models here.

class Fruits(models.Model):

    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
   
    def __str__(self):
        return self.name
        return self.quantity

class GroceryForm(ModelForm):
    class Meta:
        model = Fruits
        fields = ['name', 'quantity']

form = GroceryForm()

  


