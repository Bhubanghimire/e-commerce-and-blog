from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id =models.AutoField( primary_key=True)
    product_name =models.CharField(max_length=20)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=20, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/image",  default="")
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name
