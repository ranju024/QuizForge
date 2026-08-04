from datetime import timedelta
from django.utils import timezone

from apps.quiz.models import QuizAttempt

class TimerService:
    @staticmethod
    def remaining_seconds(attempt: QuizAttempt) -> int:
        end_time = (
            attempt.started_at + 
            timedelta(minutes=attempt.quiz.duration_minutes)
        )
        remaining = (
            end_time - timezone.now()
        ).total_seconds()

        return max(0, int(remaining))
    
    @staticmethod
    def is_expired(attempt: QuizAttempt) -> bool:
        return (
            TimerService.remaining_seconds(attempt, ) == 0
        )