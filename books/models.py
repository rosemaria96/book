from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(primary_key = True)
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length = 100)
    price = models.FloatField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.book_name
    