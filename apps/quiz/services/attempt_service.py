from django.db import transaction

from apps.accounts.models import User
from apps.quiz.models import Quiz, QuizAttempt
from .quiz_generator import QuizGenerator

class AttemptService:

    @staticmethod
    @transaction.atomic
    def start_quiz(user: User, quiz: Quiz):

        attempt = QuizAttempt.objects.create(user=user, quiz=quiz,)
        questions = QuizGenerator.get_questions(quiz)
        attempt.questions.set(questions)

        return attempt