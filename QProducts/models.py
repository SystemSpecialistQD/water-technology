from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image1 = models.ImageField(upload_to='./static/QProducts/images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='./static/QProducts/images/', blank=True, null=True)

    def __str__(self):
        return self.title