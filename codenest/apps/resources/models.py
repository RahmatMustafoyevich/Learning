from django.db import models


class Resource(models.Model):
    class Type(models.TextChoices):
        CODE = "code", "Dastur kodi"
        EBOOK = "ebook", "Elektron kitob"

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=Type.choices)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="resources/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
