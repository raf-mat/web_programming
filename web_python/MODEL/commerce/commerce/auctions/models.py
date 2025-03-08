from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=70)
    description = models.CharField(max_length=256)
    starting_bid = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Bids():
    pass

class Comments():
    pass

