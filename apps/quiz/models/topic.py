from django.db import models
from django.utils.text import slugify

from apps.core.models import TimeStampedModel
from .subject import Subject

class Topic(TimeStampedModel):
    subject = models.ForeignKey(
        "quiz.Subject",
        on_delete=models.CASCADE,
        related_name="topics",
    )
    name = models.CharField(
        max_length=100,
    )
    slug = models.SlugField(
        max_length=120,
        blank=True,
    )
    description = models.TextField(blank=True,)
    order = models.PositiveBigIntegerField(
        default=1, 
        help_text="Display order within a subject.",
    )
    is_active = models.BooleanField(default=True,)

    class Meta:
        ordering = ["subject", "order", "name"]
        constraints = [
            models.UniqueConstraint(
                fields=["subject", "name"],
                name="unique_topic_per_subject",
            ),
            models.UniqueConstraint(
                fields=["subject", "slug"],
                name="unique_topic_slug_per_subject",
            ),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.subject.name} → {self.name}"