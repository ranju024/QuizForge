from django.db.models import Max

from apps.quiz.models import QuizAttempt


class DashboardService:

    @staticmethod
    def best_attempt(user, quiz):

        return (
            QuizAttempt.objects.filter(
                user=user,
                quiz=quiz,
            )
            .aggregate(Max("percentage"))
            .get("percentage__max")
            or 0
        )