from apps.quiz.models import QuizAttempt


class ResultService:

    @staticmethod
    def finish_attempt(attempt: QuizAttempt):

        answers = attempt.answers.all()

        total_marks = sum(
            answer.question.marks
            for answer in answers
        )

        obtained_marks = sum(
            answer.question.marks
            for answer in answers
            if answer.is_correct
        )

        percentage = (
            (obtained_marks / total_marks) * 100
            if total_marks
            else 0
        )

        attempt.score = obtained_marks
        attempt.percentage = percentage
        attempt.passed = (
            percentage >= attempt.quiz.pass_percentage
        )

        attempt.finish()
        attempt.save(
            update_fields=[
                "score",
                "percentage",
                "passed",
            ]
        )

        return attempt