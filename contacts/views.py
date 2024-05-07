from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    """
    API view to list all contacts and create a new contact.
    Handles GET and POST requests.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a contact.
    Handles GET, PUT, PATCH, and DELETE requests.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    