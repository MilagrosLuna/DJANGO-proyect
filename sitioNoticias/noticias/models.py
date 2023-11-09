from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=40, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(
        default=timezone.now()
    )
    published_at = models.DateField(
        blank=True, null=True
    )

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

