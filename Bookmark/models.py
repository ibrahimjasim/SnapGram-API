from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Bookmark(models.Model):
    """
    A model for creating bookmarks by users. Ensures a user cannot bookmark a post more than once.
    It is related to both the User model and the Post model.
    """
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_at']  
        constraints = [
            models.UniqueConstraint(fields=['owner', 'post'], name='unique_bookmark')
        ]
        
    
    def __str__(self):
        return f'{self.owner.username} bookmarked "{self.post.title}"'
