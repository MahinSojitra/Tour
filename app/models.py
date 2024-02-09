from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
import uuid

class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ["MALE", "Male"], 
        ["FEMALE", "Female"]
    )
    
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    username = models.CharField(_("username"), max_length=50, unique=True)
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    birth_date = models.DateField(_("date of birth"), null=True)
    gender = models.CharField(_("gender"), max_length=10, choices=GENDER_CHOICES)
    city = models.CharField(_("city"), max_length=100)
    contact = models.CharField(_("contact no"), max_length=10, unique=True)
    pincode = models.CharField(_("pincode"), max_length=6, default="380009")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'contact']
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
class Traveler(models.Model):
    
    GENDER_CHOICES = (
        ["MALE", "Male"], 
        ["FEMALE", "Female"]
    )
    
    travelerID = models.CharField(_("traveler ID"), max_length=6, primary_key=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(_("full name"), null=False, max_length=100)
    email = models.EmailField(_("email address"), null=False, max_length=255, unique=True)
    gender = models.CharField(_("gender"), null=False, max_length=10, choices=GENDER_CHOICES)
    contact = models.CharField(_("contact no"), null=False, max_length=10, unique=True)
    birth_date = models.DateField(_("date of birth"), null=False)
    date_added = models.DateField(auto_now_add=True)
    
    def getUniqueTravelerID(self):
        unique_id = str(uuid.uuid4().hex)[:6]
        return unique_id
    
    def __str__(self):
        return self.name
    
class Place(models.Model):
    
    RATINGS_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    ]
    
    placeID = models.CharField(_("place ID"), max_length=6, primary_key=True)
    name = models.CharField(_("place name"), max_length=100)
    description = models.TextField(_("description"))
    location = models.CharField(_("location"), max_length=255)
    rating = models.CharField(_("ratings"), max_length=1, choices=RATINGS_CHOICES)
    map_url = models.URLField(_("map URL"), max_length=200)
    date_added = models.DateField(auto_now_add=True)
    
    def getUniquePlaceID(self):
        unique_id = str(uuid.uuid4().hex)[:6]
        return unique_id
    
    def __str__(self):
        return self.name

class PlaceImage(models.Model):
    imageID = models.CharField(_("image ID"), max_length=6, primary_key=True)
    place = models.ForeignKey(Place, null=False, on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to='images/')
    description = models.TextField(_("image description"))
    date_added = models.DateField(auto_now_add=True)
    
    def getUniqueImageID(self):
        unique_id = str(uuid.uuid4().hex)[:6]
        return unique_id
    
    def __str__(self):
        return self.imageID
    
class Hotel(models.Model):
    
    RATINGS_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    ]
    
    hotelID = models.CharField(_("hotel ID"), max_length=6, primary_key=True)
    name = models.CharField(_("hotel name"), max_length=100)
    description = models.TextField(_("description"))
    location = models.CharField(_("location"), max_length=255)
    facilities = models.CharField(_("facilities"), max_length=255)
    contact = models.CharField(_("contact no"), null=False, max_length=10, unique=True)
    website_url = models.URLField(_("website URL"), max_length=200)
    rating = models.CharField(_("ratings"), max_length=1, choices=RATINGS_CHOICES)
    date_added = models.DateField(auto_now_add=True)
    
    def getUniqueHotelID(self):
        unique_id = str(uuid.uuid4().hex)[:6]
        return unique_id
    
    def __str__(self):
        return self.name

class HotelImage(models.Model):
    imageID = models.CharField(_("image ID"), max_length=6, primary_key=True)
    hotel = models.ForeignKey(Hotel, null=False, on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to='images/')
    description = models.TextField(_("image description"))
    date_added = models.DateField(auto_now_add=True)
    
    def getUniqueImageID(self):
        unique_id = str(uuid.uuid4().hex)[:6]
        return unique_id
    
    def __str__(self):
        return self.imageID
    
class Package(models.Model):
    
    INCLUSION_CHOICES = [
        ("Guided city tours", "Guided city tours"),
        ("Adventure excursions (hiking, zip-lining)", "Adventure excursions (hiking, zip-lining)"),
        ("Relaxing spa day", "Relaxing spa day"),
        ("Water sports (snorkeling, kayaking)", "Water sports (snorkeling, kayaking)"),
        ("Attend a traditional dance or music performance", "Attend a traditional dance or music performance"),
        ("Visit local museums and art galleries", "Visit local museums and art galleries"),
        ("Explore historical landmarks and monuments", "Explore historical landmarks and monuments"),
        ("Private chauffeur service", "Private chauffeur service"),
        ("Local public transportation pass", "Local public transportation pass"),
        ("Group guided bus tours", "Group guided bus tours"),
        ("Rental car for self-exploration", "Rental car for self-exploration"),
        ("Photography or language guide services", "Photography or language guide services"),
        ("Scuba diving to explore underwater life", "Scuba diving to explore underwater life"),
        ("Jet skiing or parasailing", "Jet skiing or parasailing"),
        ("Snorkeling in crystal-clear waters", "Snorkeling in crystal-clear waters"),
        ("Snow or water skiing adventures", "Snow or water skiing adventures"),
        ("Mountain biking or cycling tours", "Mountain biking or cycling tours")
    ]
    
    packageID = models.CharField(_("package ID"), max_length=6, primary_key=True)
    name = models.CharField(_("package name"), max_length=100)
    places = models.ManyToManyField(Place, blank=False)
    description = models.TextField(_("description"))
    journey_start_date = models.DateField()
    duration = models.CharField(_("duration"), max_length=50)
    meals = models.CharField(_("meals"), max_length=50)
    hotels = models.ManyToManyField(Hotel, blank=False)
    price = models.CharField(_("price"), max_length=50)
    # inclusions = MultiSelectField(_("inclusions items"), max_length=255, choices=INCLUSION_CHOICES)
    max_travelers = models.IntegerField(_("no of travelers are allowed"))
    is_cancelable = models.BooleanField(_("cancelable"), default=False)
    date_added = models.DateField(auto_now_add=True)
    
    def getUniquePackageID(self):
        unique_id = str(uuid.uuid4().hex)[:6]
        return unique_id
    
    def __str__(self):
        return self.name

class Review(models.Model):
    
    RATINGS_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    ]
    
    reviewID = models.CharField(_("review ID"), max_length=6, primary_key=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, null=False, on_delete=models.CASCADE)
    rating = models.CharField(_("ratings"), max_length=1, choices=RATINGS_CHOICES)
    comment = models.CharField(_("comment"), max_length=200)
    date_posted = models.DateField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'package'], name='unique_user_package_review')
        ]
    
    def getUniqueReviewID(self):
        unique_id = str(uuid.uuid4().hex)[:6]
        return unique_id

class ContactRequest(models.Model):
    requestID = models.CharField(_("request ID"), max_length=6, primary_key=True)
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    date_added = models.DateField(auto_now_add=True)
    
    def getUniqueRequestID(self):
        unique_id = str(uuid.uuid4().hex)[:6]
        return unique_id
    
    def __str__(self):
        return self.first_name
