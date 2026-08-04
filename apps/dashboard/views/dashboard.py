from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Max, Count
from django.views.generic import TemplateView

from apps.quiz.models import Quiz, QuizAttempt
from apps.quiz.models.attempt import AttemptStatus

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        attempts = QuizAttempt.objects.filter(user=self.request.user, )
        completed = attempts.filter(status=AttemptStatus.COMPLETED, )
        context["available_quizzes"] = Quiz.objects.filter(is_active=True,)
        context["active_attempts"] = attempts.filter(
            status=AttemptStatus.IN_PROGRESS,
        ).select_related("quiz")

        context["completed_attempts"] = completed.select_related(
            "quiz",
        ).order_by("-started_at")[:5]

        context["total_attempts"] = attempts.count()
        
        context["completed_count"] = completed.count()
        context["passed_count"] = completed.filter(passed=True,).count()

        context["average_score"] = (
            completed.aggregate(
                Avg("percentage")
            )["percentage__avg"] or 0
        )

        context["best_score"] = (
            completed.aggregate(
                Max("percentage")
            )["percentage__max"]
            or 0
        )

        context["quiz_count"] = Quiz.objects.filter(is_active=True, ).count()
        
        return context
        

