from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.quiz.models import Quiz, QuizAttempt
from apps.quiz.models.attempt import AttemptStatus

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available_quizzes"] = Quiz.objects.filter(is_active=True,)
        context["active_attempts"] = QuizAttempt.objects.filter(
            user=self.request.user,
            status=AttemptStatus.IN_PROGRESS,
        ).select_related("quiz")

        context["completed_attempts"] = QuizAttempt.objects.filter(
            user=self.request.user,
            status=AttemptStatus.COMPLETED,
        ).select_related("quiz").order_by("-started_at")[:5]

        context["total_attempts"] = QuizAttempt.objects.filter(
            user=self.request.user).count()
        
        context["completed_count"] = QuizAttempt.objects.filter(
            user=self.request.user, status=AttemptStatus.COMPLETED,).count()
        
        return context
        

