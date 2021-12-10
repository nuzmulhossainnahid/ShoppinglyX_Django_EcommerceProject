from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
    ('Select Your State','Select Your State'),
    ('Dhaka', 'Dhaka'),
    ('Chotogram', 'Chotogram'),
    ('Salete', 'Salete'),
    ('Joypurhat', 'Joypurhat')
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptob'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
)

BRAND_CHOICE = (
    ('S', 'SAMSUNG'),
    ('O', 'OPPO'),
    ('A', 'APPLE'),
    ('V', 'VIVO'),
    ('T', 'TOP WERE'),
    ('B', 'BOTTOM WERE'),
    ('D', 'DELL'),
    ('AS', 'ASUS'),
    ('H', 'HP'),
    ('DL', 'DELL'),
    ('TO', 'TOSHIBA')
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField( choices=BRAND_CHOICE, max_length=20)
    category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICRS = (
    ('Accepted', 'Accepted'),
    ('packed','packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class orderPlacrd(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quentity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,
    choices=STATUS_CHOICRS, default='pending')

    @property
    def total_cost(self):
        return self.quentity * self.product.discounted_price
