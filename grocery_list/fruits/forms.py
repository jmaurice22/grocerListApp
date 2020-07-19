from django import forms
from django.forms import ModelForm

from fruits.models import Fruits


class ItemForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields = '__all__'