from django.db import models

# Create your models here.


class Pharmacy(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    pharma_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    licence = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    alternative_email = models.EmailField(max_length=254, blank=True, unique=True)
    number = models.IntegerField(blank=True, null=True)
    alternative_number = models.IntegerField(blank=True, null=True)
    date_created = models.TextField(blank=True)
    attach = models.ImageField(upload_to='media/pharmacy', blank=True, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name+"'s "+self.pharma_name+" pharmacy"

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    code = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 , null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2 , null=True)
    dom = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/pharmacy')
    approved = models.BooleanField(default=False)
    live_product = models.BooleanField(default=False)
    unapproved = models.BooleanField(default=False)
    # orders
    approved_order = models.BooleanField(default=False)
    delivered_order = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
