from django.contrib import admin

from apps.quiz.models import Choice

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "order",
        "is_correct",
    )
    list_filter = (
        "is_correct",
    )
    search_fields = ("text", )