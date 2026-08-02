from django.db import models

from .attempt import QuizAttempt
from .question import Question
from .choice import Choice

class Answer(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choices = models.ManyToManyField(Choice, blank=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["attempt", "question"],
                name="unique_answer_per_question",
            )
        ]

    def __str__(self):
        return f"{self.attempt} - {self.question.external_id}"
    
