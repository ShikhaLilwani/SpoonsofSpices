from django.db import models

# Create your models here.
class RecipeTable(models.Model):
    CATEGORIES=((1,'VEG'),(2,'NONVEG'))
    name=models.CharField(max_length=50)
    time=models.FloatField()
    details=models.CharField(max_length=100)
    category=models.IntegerField(choices=CATEGORIES)
    is_active=models.BooleanField()
    rating=models.FloatField()

def __str__(self):
    return self.name+"added to cart"