from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.quiz.models import QuizAttempt

class MyAttemptsView(LoginRequiredMixin, ListView):
    model = QuizAttempt
    template_name = "dashboard/my_attempts.html"
    context_object_name = "attempts"
    paginate_by = 10

    def get_queryset(self):
        return (
            QuizAttempt.objects.filter(user=self.request.user, 
            ).select_related("quiz").order_by("-started_at")
        )
    