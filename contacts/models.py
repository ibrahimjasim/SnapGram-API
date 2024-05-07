from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    Contact model for storing contact information related to a user.
    Includes fields for name, email, phone, address, and a message.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    message = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of
        the contact, including its ID and name.
        """
        return f'{self.id} {self.name}'
