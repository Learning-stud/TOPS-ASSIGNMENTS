# myapp/models.py

from django.db import models

class ProductMst(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)

class ProductSubCat(models.Model):
    product = models.ForeignKey(ProductMst, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    model = models.CharField(max_length=50)
    ram = models.CharField(max_length=10)
