from django.db import models

class Flavor(models.Model):
    name=models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    image_url = models.URLField()
    is_best_seller = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create your models here.
