from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from apps.quiz.forms import AnswerForm
from apps.quiz.models import QuizAttempt
from apps.quiz.services import (AnswerService, ResultService, )

class TakeQuizView(LoginRequiredMixin, View):
    def get(self, request, attempt_id, question_no):
        attempt = get_object_or_404(
            QuizAttempt,
            pk=attempt_id,
            user=request.user,
        )
        questions = list(
            attempt.questions.all()
        )
        if question_no < 1 or question_no > len(questions):
            return redirect(
                "quiz:detail",
                attempt.quiz.pk,
            )
        question = questions[question_no - 1]
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
                "total_questions": len(questions),
            },
        )
        
    def post(self, request, attempt_id, question_no):
        attempt = get_object_or_404(
            QuizAttempt,
            pk=attempt_id,
            user=request.user,
        )
        questions = list(
            attempt.questions.all()
        )
        question = questions[question_no - 1]
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
                    "total_questions": len(questions),
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
        if question_no == len(questions):
            ResultService.finish_attempt(
                attempt,
            )
            return redirect(
                "quiz:detail",
                attempt.quiz.pk,
            )
        return redirect(
            "quiz:take",
            attempt_id=attempt.pk,
            question_no=question_no + 1,
        )