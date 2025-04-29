from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Follow(models.Model):

    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('following', 'followed')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.following.username} → {self.followed.username}"