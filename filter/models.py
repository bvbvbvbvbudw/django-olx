from django.db import models

# Create your models here.
class Filter(models.Model):
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, null=True, blank=True, default='https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/1665px-No-Image-Placeholder.svg.png')
    description = models.TextField()
