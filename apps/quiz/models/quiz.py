from django.db import models

from apps.core.models import TimeStampedModel
from .topic import Topic


class Quiz(TimeStampedModel):
    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    topics = models.ManyToManyField(
        Topic,
        related_name="quizzes",
    )

    duration_minutes = models.PositiveIntegerField(default=30)

    total_questions = models.PositiveIntegerField(default=20)

    pass_percentage = models.PositiveSmallIntegerField(default=50)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title