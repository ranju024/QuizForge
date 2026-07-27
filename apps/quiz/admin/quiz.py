from django.contrib import admin

from apps.quiz.models import Quiz


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "duration_minutes",
        "total_questions",
        "pass_percentage",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
    )

    filter_horizontal = (
        "topics",
    )