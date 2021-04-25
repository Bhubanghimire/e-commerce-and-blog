from django.db import models

# Create your models here.
class Product(models.Model):
    id =models.AutoField(primary_key=True)
    product_name =models.CharField(max_length=20)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=20, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/image")
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField( primary_key=True )
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=20)
    Phone = models.IntegerField()
    Address =models.CharField(max_length=20)
    Message = models.CharField(max_length=500)

    def __str__(self):
        return self.Name

class Order(models.Model):
    Order_id =  models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Item_jason = models.CharField(max_length=400)
    District = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Phone = models.IntegerField()

    def __str__(self):
        return self.Name

class OrderUpdate(models.Model):
    Update_id = models.AutoField(primary_key=True)
    Order_id = models.IntegerField(default="")
    Update_desc = models.CharField(max_length=500)
    TimeStamp = models.DateField( auto_now_add= True)

    def __str__(self):
        return self.Update_desc[0:7]+"..."