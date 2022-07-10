from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(max_length= 100)
    author_name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits= 10, decimal_places= 2 )


    class Meta:
        model = Book
        fields = ('__all__')