from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model to store additional information about users.
    It has a one-to-one relationship with the User model.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_fqfn5s')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of this profile,
        featuring the username of the associated user.
        """
        return f"{self.owner.username}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler that creates a Profile instance automatically
    whenever a new User instance is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
