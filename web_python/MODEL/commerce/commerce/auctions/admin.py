from django.contrib import admin
from  .models import AuctionListing
# Register your models here.

class AuctionListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(AuctionListing, AuctionListingAdmin)