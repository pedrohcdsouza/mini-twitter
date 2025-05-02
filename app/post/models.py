from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import os

@deconstructible

class UploadToPathAndRename:
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{instance.id if instance.id else 'temp'}.{ext}"
        return os.path.join('post_images', instance.author.username, filename)

path_and_rename = UploadToPathAndRename()

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to=path_and_rename, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    
class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('author', 'post')

    def __str__(self):
        return f"{self.author.username} liked {self.post.id}"