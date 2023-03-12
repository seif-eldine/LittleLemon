from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) #max_digits=10.2
    inventory = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    bookingDate = models.DateField()