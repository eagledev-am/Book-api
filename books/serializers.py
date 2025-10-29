from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookFullSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True 
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'published_date', 'author', 'author_id', 'price', 'owner']
