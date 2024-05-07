from django.db import models
from django.conf import settings
from django.utils import timezone


class Event(models.Model):
    """Represents an event within the system"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=300)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organized_events'
    )
    admission_price = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        """Return a string representation of
        the event including its title and organizer."""
        return f"{self.title} by {self.organizer.username}"

    @property
    def is_upcoming(self):
        """Check if the event is upcoming based on the current time."""
        return self.start_time > timezone.now()

    @property
    def is_past(self):
        """Check if the event has already passed based on the current time."""
        return self.end_time < timezone.now()

    @classmethod
    def upcoming_events(cls, user):
        """Return upcoming events organized by
        users followed by the requesting user."""
        followed_users = user.followed_by.all()
        return cls.objects.filter(
            organizer__in=followed_users, start_time__gt=timezone.now()
        ).order_by('start_time')
        