from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

@login_required
def inventory_list(request):
    inventories=Inventory.objects.all()
    context={
        'title':'Inventory List',
        'inventories':inventories
    }
    return render(request,'inventory_list.html',context)


@login_required
def per_product_view(request,pk):
    inventory=get_object_or_404(Inventory,pk=pk)
    context={
        'inventory':inventory
    }
    return render(request,'per_product.html',context)

@login_required
def add_product(request):
    if request.method == 'POST':
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            # Convert string values to integers for multiplication
            cost_per_item = int(add_form.cleaned_data['cost_per_item'])
            quantity_sold = int(add_form.cleaned_data['quantity_sold'])
            new_inventory.sales = cost_per_item * quantity_sold
            new_inventory.save()
            return redirect('/inventory/')
    else:
        add_form = AddInventoryForm()
    
    return render(request, 'inventory_add.html', {'form': add_form})


def delete_inventory(request,pk):
    inventory=Inventory.objects.get(pk=pk)
    inventory.delete()
    return redirect('/inventory')

def update_inventory(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    if request.method == 'POST':
        updateForm = UpdateInventoryForm(data=request.POST)
        if updateForm.is_valid():
            inventory.name = updateForm.cleaned_data['name']
            inventory.quantity_in_stock = updateForm.cleaned_data['quantity_in_stock']
            inventory.quantity_sold = updateForm.cleaned_data['quantity_sold']
            inventory.cost_per_item = updateForm.cleaned_data['cost_per_item']
            inventory.sales = inventory.cost_per_item * inventory.quantity_sold
            inventory.save()
            print(pk)
            return redirect(f'/inventory/product/{pk}')  # Redirect to inventory list page after successful update
    else:
        updateForm = UpdateInventoryForm(instance=inventory)
    
    return render(request, 'inventory_update.html', {'form': updateForm})

def sell_item(request):
    if request.method == 'POST':
        sell_form = SellItemForm(request.POST)
        if sell_form.is_valid():
            inventory_item = sell_form.cleaned_data['inventory_item']
            quantity_sold = sell_form.cleaned_data['quantity_sold']
            
            # Update inventory records
            inventory_item.quantity_in_stock -= quantity_sold
            inventory_item.quantity_sold += quantity_sold
            inventory_item.sales += inventory_item.cost_per_item * quantity_sold  # Update sales revenue
            inventory_item.save()

            # Save sales record
            SalesRecord.objects.create(inventory=inventory_item, quantity_sold=quantity_sold)

            return redirect('sell_item')  # Redirect to sell item page after successful sale
    else:
        sell_form = SellItemForm()
    
    return render(request, 'sell_item.html', {'sell_form': sell_form})