from django.db import IntegrityError
from rest_framework import serializers
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer class for handling Bookmark data. Ensures that bookmarks are uniquely created
    and handles potential duplicate bookmark attempts gracefully.
    """

    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Bookmark  
        fields = ['id', 'owner_username', 'post', 'created_at'] 
        read_only_fields = ('id', 'created_at') 

    def create(self, validated_data):
        """
        Custom create method to handle the creation of Bookmark instances,
        catching IntegrityError to handle possible duplicate entries.
        """
        try:
            
            return super().create(validated_data)
        except IntegrityError as e:
           
            raise serializers.ValidationError({'detail': 'This bookmark already exists.'}) from e