from django.db import models

# Create your models here.
class Reader(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    phone = models.IntegerField(max_length=10)

    def __str__(self) -> str:
        return self.name
    

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    genre = models.CharField(max_length=50)
    quantity = models.IntegerField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    reader = models.ManyToManyField(Reader, related_name='book')

    def __str__(self) -> str:
        return self.name
