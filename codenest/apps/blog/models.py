from django.conf import settings
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class BlogLike(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")
