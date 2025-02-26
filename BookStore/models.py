from django.db import models

# Create your models here.
class Book(models.Model):
    title= models.CharField(max_length=50)
    description= models.TextField()
    author= models.CharField(max_length=50)
    image= models.ImageField(upload_to='static/BookStore/images/',blank=True,null=True)
    file= models.FileField(upload_to='static/BookStore/books/')
    category= models.CharField(max_length=50,choices=[('guides','كتب إرشادية'),('reports','تقارير فنية'),('research','ابحاث علمية')])
    upload_date= models.DateTimeField(auto_now_add=True)
   # download_count=models.PositiveIntegerField(default=0)
   # rating=models.PositiveSmallIntegerField(default=0,choices=[(i, i) for i in range(1,6)])
    def __str__(self):
        return self.title
