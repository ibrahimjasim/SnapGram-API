from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    """"Model for UserNotification, which is triggered by activities such as
    posting, liking, commenting, or following.
    """

    NOTIFICATION_CHOICES = [
        ("follow", "Follow"),
        ("comment", "Comment"),
        ("like", "Like"),
        ("posts", "New Post"),
    ]
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORIES, max_length=50)
    item_id = models.IntegerField(null=True)
    is_read = models.BooleanField(default=False)
    content = models.CharField(max_length=255)

    class Meta:
        ordering = ["-time_created"]

    def __str__(self):
        return (
            f"{self.id} {self.get_category_display()} "
            f"notification for {self.owner}"
        )