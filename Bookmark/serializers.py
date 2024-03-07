from django.db import IntegrityError
from rest_framework import serializers
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer class for handling Bookmark data.
    """
    # Define a read-only field for the owner's username to prevent it from being set directly
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Bookmark  
        fields = ['id', 'owner_username', 'post', 'created_at']  
        read_only_fields = ('id', 'created_at')  