from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField()

    def _str_(self):
        return self.title

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'year')

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)    
