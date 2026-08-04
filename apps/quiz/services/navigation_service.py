from django.shortcuts import redirect

from apps.quiz.models import QuizAttempt

class NavigationService:
    @staticmethod
    def get_questions(attempt: QuizAttempt, question_no: int):
        questions = list(
            attempt.questions.all()
        )
        if not questions:
            return None
        answered_count = attempt.answers.count()
        expected_question = answered_count + 1

        if attempt.status == "completed":
            return redirect(
                "quiz:result",
                pk=attempt.pk,
            )
        
        if (question_no < 1 or question_no > len(questions)):
            return redirect(
                "quiz:take",
                attempt_id=attempt.pk,
                question_no=expected_question,
            )
        if question_no != expected_question:
            return redirect(
                "quiz:take",
                attempt_id=attempt.pk,
                question_no=expected_question,
            )

        return questions[question_no - 1]