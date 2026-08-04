from django.db import transaction

from apps.accounts.models import User
from apps.quiz.models import Quiz, QuizAttempt
from apps.quiz.models.attempt import AttemptStatus
from .quiz_generator import QuizGenerator

class AttemptService:

    @staticmethod
    @transaction.atomic
    def start_quiz(user: User, quiz: Quiz):

        attempt = QuizAttempt.objects.filter(user=user, quiz=quiz, status=AttemptStatus.IN_PROGRESS,).first()

        if attempt:
            return attempt
        
        attempt = QuizAttempt.objects.create(user=user, quiz=quiz,)
        questions = QuizGenerator.get_questions(quiz)
        attempt.questions.set(questions)

        return attempt