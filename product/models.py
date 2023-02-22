from django.db import models
from django.db.models.deletion import CASCADE
from users.models import CustomUser
# Create your models here.
class Product (models.Model):
    Id=models.AutoField(primary_key=True)
    picture=models.URLField()
    productName=models.CharField(max_length=200)
    availableQuantity=models.IntegerField()
    pricePerUnit=models.FloatField()
    description=models.TextField()

class Card (models.Model):
    Card_id=models.AutoField(primary_key=True)
    productId=models.ForeignKey(Product,CASCADE)
    userId=models.ForeignKey(CustomUser,CASCADE)
    quantity=models.IntegerField()