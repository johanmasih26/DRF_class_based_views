from django.db import models




class Book(models.Model):
    book_title = models.CharField(max_length= 100)
    author_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits= 10, decimal_places= 2 )

    def __str__(self):
        return self.book_title