from django.db import models

# Create your models here.

class Inventory(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    cost_per_item=models.IntegerField(null=False,blank=False)
    quantity_in_stock=models.IntegerField(null=False,blank=False)
    quantity_sold=models.IntegerField(null=False,blank=False)
    sales=models.IntegerField()
    stock_date=models.DateField(auto_now_add=True)
    last_sales_date=models.DateField(auto_now=True)
    
    
    class Meta:
        verbose_name_plural ='Inventories'

    def __str__(self) -> str:
        return self.name
    
# models.py
class SalesRecord(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    sale_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.inventory.name} - {self.quantity_sold} units sold on {self.sale_date}"
