from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Raises a ValidationError with a code of 'max_value'/'min_value' if value is greater than limit_value, which may be a callable.


# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiR87P28pX4AhXqwTgGHfxtDlcQFnoECA8QAw&url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fmodels%2Ffields%2F&usg=AOvVaw0QvO0ZxTIDAXYa8RnHOj19
#  list of category is a fixed or not so often updated, so we use choices 
STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andra Pradesh', 'Andra Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('U.P', 'U.P'),
    ('M.P', 'M.P'),
    ('Delhi', 'Delhi'),
    ('Maharastra','Maharastra')
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES, max_length=200)

    def __str__(self):
        return str(self.id)
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiR87P28pX4AhXqwTgGHfxtDlcQFnoECA8QAw&url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fmodels%2Ffields%2F&usg=AOvVaw0QvO0ZxTIDAXYa8RnHOj19
#  list of category is a fixed or not so often updated, so we use choices 
CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear')
)   

class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=200)
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to = 'productimg')
# str function in a django model returns a string that is exactly rendered as the display name of instances for that model.
    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1) 

    def __str__(self):
        return str(self.id)

    # helps in model template relationship
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price        

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)  

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1) 
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')


    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price        




