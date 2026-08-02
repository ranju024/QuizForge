from django.contrib import admin

from apps.quiz.models import Answer

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "attempt",
        "question",
        "is_correct",
    )
    autocomplete_fields = (
        "attempt",
        "question",
        # "selected_choices",
    )