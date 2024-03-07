from rest_framework import generics, permissions, filters
from drf_api.permissions import IsNotificationOwner
from .models import Notification
from .serializers import NotificationSerializer

class NotificationList(generics.ListAPIView):
    """Provides a listing of all notifications for the currently authenticated user.
    This endpoint does not support the creation of notifications as they are
    generated in response to specific user actions within the application, such as
    likes, comments, or follows."""

    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'is_read']

    def get_queryset(self):
        """Return notifications for the currently authenticated user."""
        return Notification.objects.filter(owner=self.request.user)


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows for retrieval, updating, or deletion of a specific notification.
    Access is restricted solely to the owner of the notification, ensuring
    privacy and security of user data. Users can manage their notifications,
    marking them as read or deleting them as necessary.
    """

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated, IsNotificationOwner]

    def get_queryset(self):
        """Override to restrict access to the notifications owned by the user."""
        return super().get_queryset().filter(owner=self.request.user)