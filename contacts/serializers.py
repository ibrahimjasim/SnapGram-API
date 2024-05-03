from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'owner', 'name', 'email', 'phone', 'address', 'message', 'created_at', 'updated_at']