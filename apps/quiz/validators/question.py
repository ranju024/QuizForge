from django.core.exceptions import ValidationError

from apps.quiz.constants import MIN_CHOICES, MAX_CHOICES
from apps.quiz.choices import QuestionType


def validate_question(question, choices):
    if len(choices) < MIN_CHOICES:
        raise ValidationError(
            f"A question must have at least {MIN_CHOICES} choices."
        )

    if len(choices) > MAX_CHOICES:
        raise ValidationError(
            f"A question can have at most {MAX_CHOICES} choices."
        )

    correct_choices = [c for c in choices if c.is_correct]

    if len(correct_choices) == 0:
        raise ValidationError(
            "At least one choice must be correct."
        )

    if (
        question.question_type == QuestionType.SINGLE_CHOICE
        and len(correct_choices) != 1
    ):
        raise ValidationError(
            "Single choice questions must have exactly one correct answer."
        )

    texts = [c.text.strip().lower() for c in choices]

    if len(texts) != len(set(texts)):
        raise ValidationError(
            "Duplicate choices are not allowed."
        )