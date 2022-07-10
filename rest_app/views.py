from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class IndexView(View):

     def get(self, request, *args, **kwargs):
         return render(request, 'index.html')

class BookView(APIView):

    def get_queryset(self, request, id = None):
        book = get_object_or_404(Book, id =id)
        serializer = BookSerializer(book,many =False)
        return Response({'data':serializer.data})
    
    def get(self, request, id = None):
        
        books = Book.objects.all()
        serializer = BookSerializer(books,many =True)
        return Response({'data':serializer.data})

    def post(self, request,id =None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def patch(self, request, id):
        book_id = Book.objects.get(id=id)
        serializer = BookSerializer(book_id, request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data}, status = status.HTTP_201_CREATED )
        else:
            return Response({"status": "error", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    
    def delete(self, request, id = None):
        book_id = get_object_or_404(Book, id =id)
        book_id.delete()
        return Response({"book deleted"})