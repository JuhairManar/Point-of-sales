from .models import *
from django.forms import ModelForm
from django import forms

class AddInventoryForm(ModelForm):
    class Meta:
        model=Inventory
        fields={'name','cost_per_item','quantity_in_stock','quantity_sold'}
        
class UpdateInventoryForm(ModelForm):
    class Meta:
        model=Inventory
        fields=['name','cost_per_item','quantity_in_stock','quantity_sold']
        
class SellItemForm(forms.Form):
    inventory_item = forms.ModelChoiceField(queryset=Inventory.objects.all(), empty_label=None)
    quantity_sold = forms.IntegerField(min_value=1)
