from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model. It handles serialization for
    basic contact details including ID, owner, name, email, phone, address,
    message, and timestamps for creation and updates.
    """
    class Meta:
        model = Contact
        fields = [
            'id', 'owner', 'name', 'email', 'phone', 'address',
            'message', 'created_at', 'updated_at'
        ]
        