from django.contrib import admin
from apps.quiz.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "topic",
        "difficulty",
        "question_type",
        "marks",
        "is_active",
    )

    list_filter = (
        "difficulty",
        "question_type",
        "topic__subject",
        "is_active",
    )

    search_fields = (
        "text",
        "topic__name",
        "topic__subject__name",
    )

    autocomplete_fields = ( "topic", )
    readonly_fields = ( 
        "uuid",
        "created_at",
        "updated_at",
    )

    inlines = [ChoiceInline, ]