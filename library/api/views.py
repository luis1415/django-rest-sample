from django.shortcuts import render
from rest_framework import viewsets, filters 
from .models import Books
from .serializers import BookSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("title", "author", "publisher", "publication_year", "category")