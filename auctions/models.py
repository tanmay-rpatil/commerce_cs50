from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="category_listings")
    list_date = models.DateTimeField('date listed')

    def __str__(self):
        return self.title

class Bid(models.Model):
    parent_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    value = models.DecimalField(max_digits=12, decimal_places=2)
    bid_date = models.DateTimeField('date bidded')
    bidder = models.ForeignKey(User,on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"Bid on {self.parent_listing} by {self.bidder} for ${self.value}"



