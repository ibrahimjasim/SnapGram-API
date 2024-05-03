from django.db import models
from django.db import models
from django.conf import settings
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=300)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_events')
    admission_price = models.TextField( blank=True)  
    website = models.URLField(blank=True)  

    def __str__(self):
        return f"{self.title} by {self.organizer.username}"

    @property
    def is_upcoming(self):
        return self.start_time > timezone.now()

    @property
    def is_past(self):
        return self.end_time < timezone.now()

    @classmethod
    def upcoming_events(cls, user):
        """Returns a queryset of upcoming events organized by users followed by the requesting user.
           Assumes 'follows' field is managed elsewhere in the user model."""
        followed_users = user.followed_by.all()
        return cls.objects.filter(organizer__in=followed_users, start_time__gt=timezone.now()).order_by('start_time')