from django.db import models

from apps.core.models import TimeStampedModel
from apps.accounts.models import User
from .quiz import Quiz

class AttemptStatus(models.TextChoices):
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETED = "completed", "Completed"

class QuizAttempt(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "quiz_attempts")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="attempts")
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices = AttemptStatus.choices, default=AttemptStatus.IN_PROGRESS)
    passed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-started_at"]
    
    def __str__(self):
        return f"{self.user.email} - {self.quiz.title}"
    