from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from apps.quiz.models import QuizAttempt


class ResultView(LoginRequiredMixin, DetailView):
    model = QuizAttempt
    template_name = "quiz/result.html"
    context_object_name = "attempt"

    def get_queryset(self):
        return QuizAttempt.objects.filter(
            user=self.request.user,
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = self.object.answers.select_related(
            "question",
        ).prefetch_related(
            "selected_choices",
            "question__choices",
        )
        total_marks = sum(
            answer.question.marks for answer in answers
        )
        obtained_marks = sum(
            answer.question.marks
            for answer in answers
            if answer.is_correct
        )
        percentage = (
            obtained_marks * 100 / total_marks
            if total_marks 
            else 0
        )

        context["answers"] = answers
        context["total_marks"] = total_marks
        context["obtained_marks"] = obtained_marks
        context["percentage"] = round(percentage, 2)

        return context
