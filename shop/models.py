from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id =models.AutoField( primary_key=True)
    product_name =models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.product_name
