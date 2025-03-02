from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=70)
    description = models.CharField(max_length=256)
    starting_bid = models.IntegerField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)

    def __str__(self):
        return f"{self.title}"

class Bids():
    pass

class Comments():
    pass

