from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Truck(models.Model):

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class  IceCreamFlavor(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class ProductMixin(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    sold = models.IntegerField(default=0)
    truck = models.ForeignKey(Truck,on_delete=models.CASCADE)
    

    class Meta:
        abstract = True 

class  IceCream (ProductMixin):
    flavor = models.ForeignKey(IceCreamFlavor,on_delete=models.CASCADE) 

class  ShavedIce (ProductMixin):
    pass

class  Snackbar (ProductMixin):
    pass     

