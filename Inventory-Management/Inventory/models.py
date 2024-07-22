from django.db import models

class Item(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=100,unique=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    category    = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    item     = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE) # Uncomment this line when Warehouse model is created

    def __str__(self):
        return self.item.name