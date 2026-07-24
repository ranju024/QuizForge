from apps.quiz.validators.question import validate_question


class QuestionService:

    @staticmethod
    def validate(question, choices):
        validate_question(question, choices)