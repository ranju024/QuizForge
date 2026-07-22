from django.db import models

from apps.core.models import TimeStampedModel
from .question import Question

class Choice(TimeStampedModel):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices",

    )
    text = models.CharField(max_length=500,)
    is_correct = models.BooleanField(default=False,)
    order = models.PositiveSmallIntegerField(default=1,)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.text