from django.contrib import admin
from .models import User, ContactRequest, Traveler, PlaceImage, Place, Hotel, HotelImage, Package, Review

# Register your models here.
admin.site.register(User)
admin.site.register(ContactRequest)
admin.site.register(Traveler)
admin.site.register(Place)
admin.site.register(Hotel)
admin.site.register(HotelImage)
admin.site.register(Package)
admin.site.register(Review)

@admin.register(PlaceImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["imageID", "image", "description", "date_added"]