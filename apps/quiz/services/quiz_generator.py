import random

from apps.quiz.models import Quiz, Question

class QuizGenerator:

    @staticmethod
    def get_questions(quiz: Quiz):

        questions = Question.objects.filter(
            topic__in=quiz.topics.all(),
            is_active=True,
        ).prefetch_related("choices")

        questions = list(questions)

        if quiz.randomize_questions:
            random.shuffle(questions)

        return questions[:quiz.total_questions]