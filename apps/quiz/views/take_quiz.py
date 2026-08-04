from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.quiz.forms import AnswerForm
from apps.quiz.models import QuizAttempt
from apps.quiz.services import (AnswerService, ResultService, NavigationService, TimerService, )

class TakeQuizView(LoginRequiredMixin, View):
    def get(self, request, attempt_id, question_no):
        attempt = get_object_or_404(
            QuizAttempt,
            pk=attempt_id,
            user=request.user,
        )
        
        question = NavigationService.get_questions(
            attempt,
            question_no,
        )

        if TimerService.is_expired(attempt):
            ResultService.finish_attempt(
                attempt,
            )

            return redirect(
                "quiz:result",
                pk=attempt.pk,
            )
        remaining_seconds = (
            TimerService.remaining_seconds(
                attempt,
            )
        )
        
        if not hasattr(question, "id"):
            return question

        form = AnswerForm(
            question=question,
        )

        return render(
            request,
            "quiz/take_quiz.html",
            {
                "attempt": attempt,
                "question": question,
                "form": form,
                "question_no": question_no,
                "total_questions": attempt.questions.count(),
                "remaining_seconds": remaining_seconds,
            },
        )
        
    def post(self, request, attempt_id, question_no):
        attempt = get_object_or_404(
            QuizAttempt,
            pk=attempt_id,
            user=request.user,
        )
        if TimerService.is_expired(attempt):
            ResultService.finish_attempt(
                attempt,
            )

            return redirect(
                "quiz:result",
                pk=attempt.pk,
            )
        question = NavigationService.get_questions(
            attempt,
            question_no,
        )

        if not hasattr(question, "id"):
            return question

        form = AnswerForm(
            request.POST,
            question=question,
        )

        if not form.is_valid():
            return render(
                request,
                "quiz/take_quiz.html",
                {
                    "attempt": attempt,
                    "question": question,
                    "form": form,
                    "question_no": question_no,
                    "total_questions": attempt.questions.count(),
                },
            )

        selected = form.cleaned_data["choices"]

        AnswerService.submit_answer(
            attempt=attempt,
            question=question,
            selected_choice_ids=(
                [selected.id]
                if question.question_type == "single_choice"
                else [choice.id for choice in selected]
            ),
        )

        if question_no == attempt.questions.count():
            ResultService.finish_attempt(attempt)

            return redirect(
                "quiz:result",
                pk=attempt.pk,
            )

        return redirect(
            "quiz:take",
            attempt_id=attempt.pk,
            question_no=question_no + 1,
        )