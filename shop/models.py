from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(default="")

    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_created=True, auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    facility = models.ForeignKey('facilities.Facility', blank=True, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    available = models.BooleanField(default=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/images/')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     # self.created_by = self.request.user
    #     return super(Product, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    paid = models.BooleanField(default=False)
    amount = models.FloatField()

    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=False, related_name='order_items')
    quantity = models.IntegerField(default=0)

    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return f"Order - {self.order.id}"


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=False)
    amount = models.FloatField()

    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_on = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return f"Order - {self.order.id}"
