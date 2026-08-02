from apps.quiz.models import (
    Answer,
    Choice,
    Question,
    QuizAttempt,
)


class AnswerService:

    @staticmethod
    def submit_answer(
        attempt: QuizAttempt,
        question: Question,
        selected_choice_ids: list[int],
    ):

        selected_choices = Choice.objects.filter(
            id__in=selected_choice_ids,
        )

        correct_choices = question.choices.filter(
            is_correct=True,
        )

        is_correct = (
            set(selected_choices.values_list("id", flat=True))
            ==
            set(correct_choices.values_list("id", flat=True))
        )

        answer, _ = Answer.objects.update_or_create(
            attempt=attempt,
            question=question,
            defaults={
                "is_correct": is_correct,
            },
        )

        answer.selected_choices.set(selected_choices)

        return answer