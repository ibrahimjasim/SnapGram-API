from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    """This model represents an automatically 
    generated notification sent to a user. It is 
    triggered and dynamically generated in response tovarious user interactions such as 
     creating posts, liking content, commenting, and following other users.
    """

    CATEGORIES = [
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
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.id} {self.get_category_display()} "
            f"notification for {self.owner}"
        )