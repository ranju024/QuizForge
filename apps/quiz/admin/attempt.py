from django.contrib import admin

from apps.quiz.models import QuizAttempt

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "quiz",
        "score",
        "passed",
        "status",
        "started_at",
    )
    list_filter = (
        "status",
        "passed",
    )
    autocomplete_fields = (
        # "user",
        "quiz",
    )
    search_fields = (
        # "user__email",
        "quiz__title",
    )