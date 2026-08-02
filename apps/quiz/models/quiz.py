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
    
    duration_minutes = models.PositiveIntegerField(default=30, help_text="Duration in minutes",)

    total_questions = models.PositiveIntegerField(default=10)

    pass_percentage = models.PositiveSmallIntegerField(default=40)

    is_active = models.BooleanField(default=True)
    randomize_questions = models.BooleanField(default=True)
    randomize_choices = models.BooleanField(default=True,)
    is_active = models.BooleanField(default=True,)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title