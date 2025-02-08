from rest_framework import serializers
from .models import Reader, Book


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['id', 'name', 'email', 'phone', 'book']

    #book = serializers.StringRelatedField(many=True)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'genre', 'quantity', 'price', 'reader']

    reader = serializers.StringRelatedField(many=True)