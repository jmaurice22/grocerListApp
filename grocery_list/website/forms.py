from django.forms import ModelForm
from fruits.models import Fruits

class GroceryForm(ModelForm):
    class Meta:
        model = Fruits
        fields = ['name', 'quantity']

form = GroceryForm()