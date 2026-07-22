from django.db import models

from apps.core.models import TimeStampedModel
from .topic import Topic
from apps.quiz.choices import Difficulty, QuestionType


class Question(TimeStampedModel):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="questions",
    )
    text = models.TextField()
    code_snippet = models.TextField(blank=True,) # for questions that need code

    explanation = models.TextField(blank=True,)
    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        default=Difficulty.MEDIUM,
    )
    question_type = models.CharField(
        max_length=20,
        choices=QuestionType.choices,
        default=QuestionType.SINGLE_CHOICE,
    )
    marks = models.PositiveSmallIntegerField(default=1,)
    is_active = models.BooleanField(default=True,)

    class Meta:
        ordering = ["topic", "id"]
        indexes = [
            models.Index(fields=["topic"]),
            models.Index(fields=["difficulty"]),
            models.Index(fields=["is_active"]),
        ]

    def __str__(self):
        return self.text[:75] if self.text else f"Question #{self.pk}"