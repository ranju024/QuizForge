from django.views.generic import ListView, DetailView

from apps.quiz.models import Quiz, QuizAttempt
from apps.quiz.models.attempt import AttemptStatus

class QuizListView(ListView):
    model = Quiz
    template_name = "quiz/quiz_list.html"
    context_object_name = "quizzes"

    def get_queryset(self):
        return Quiz.objects.filter(is_active=True,)
    
class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quiz/quiz_detail.html"
    context_object_name = "quiz"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:

            active_attempt = QuizAttempt.objects.filter(
                user=self.request.user,
                quiz=self.object,
                status=AttemptStatus.IN_PROGRESS,
            ).first()

            context["active_attempt"] = active_attempt

            context["attempts"] = QuizAttempt.objects.filter(
                user=self.request.user,
                quiz=self.object,
            ).order_by("-started_at")

        return context