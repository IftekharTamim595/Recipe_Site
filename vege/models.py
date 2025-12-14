from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_photos/')
    
    def __str__(self):
        return self.name
