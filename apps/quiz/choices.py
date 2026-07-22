from django.db import models


class Difficulty(models.TextChoices):
    EASY = "easy", "Easy"
    MEDIUM = "medium", "Medium"
    HARD = "hard", "Hard"


class QuestionType(models.TextChoices):
    SINGLE_CHOICE = "single", "Single Choice"
    MULTIPLE_CHOICE = "multiple", "Multiple Choice"