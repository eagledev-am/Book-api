from urllib import request
from xmlrpc.client import DateTime
from django.http import Http404
from django.shortcuts import render
from rest_framework import status , viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AuthorSerializer, BookFullSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly

from .models import Author, Book




class BookList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        books = Book.objects.all()
        serialized_books = BookFullSerializer(books, many=True)
        return Response(serialized_books.data , status=status.HTTP_200_OK)
    
    def post(self,request):
        serialized_book = BookFullSerializer(data=request.data)
        if serialized_book.is_valid():
            serialized_book.save()
            return Response(serialized_book.data, status=status.HTTP_201_CREATED)
        return Response(serialized_book.errors , status=status.HTTP_400_BAD_REQUEST)
    

class BookDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_object(self, book_id):
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request , id):
        book = self.get_object(id)
        serialized_book = BookFullSerializer(book)
        return Response(serialized_book.data , status=status.HTTP_200_OK)

    def put(self , request , id):
        book = self.get_object(id)
        serialized_book = BookFullSerializer(book , request.data , partial=True)
        
        if serialized_book.is_valid():
            serialized_book.save()
            return Response(serialized_book.data, status=status.HTTP_200_OK)
        return Response(serialized_book.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , id):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]