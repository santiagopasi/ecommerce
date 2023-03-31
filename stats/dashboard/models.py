from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
User = settings.AUTH_USER_MODEL
CATEGORIES=(

    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food')
)
class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=20,choices=CATEGORIES,null=True)
    quantity = models.PositiveBigIntegerField(null=True)

    def last_product_added(self):
        return f'Last product added: {self.name} - {self.quantity} units available.'.capitalize()
    def __str__(self):
        return f'{self.name}'.capitalize()
    

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(User, on_delete=models.CASCADE,null=True )
    order_quantity=models.PositiveBigIntegerField(null=True)
    date=models.DateField(auto_now_add=True)

    