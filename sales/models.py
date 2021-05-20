from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class ProductPrice(models.Model):
    product = models.ForeignKey(Product, related_name='prices', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=3,max_digits=20)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.price)