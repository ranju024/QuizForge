from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from apps.quiz.models import Quiz
from apps.quiz.services import AttemptService

class StartQuizView(LoginRequiredMixin, View):

    def post(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk, is_active=True,)
        attempt = AttemptService.start_quiz(request.user, quiz, )
        answered_count = attempt.answers.count()
        return redirect("quiz:take", attempt_id=attempt.pk, question_no=answered_count + 1,)
    