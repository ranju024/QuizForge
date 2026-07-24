from django.contrib import admin

from apps.quiz.admin.forms import ChoiceInlineFormSet
from apps.quiz.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    formset = ChoiceInlineFormSet
    extra = 2
    min_num = 2

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "topic",
        "difficulty",
        "question_type",
        "marks",
        "is_active",
    )

    list_filter = (
        "topic",
        "difficulty",
        "question_type",
        "is_active",
    )

    search_fields = (
        "text",
        "topic__name",
        # "topic__subject__name",
    )

    autocomplete_fields = ( "topic", )
    readonly_fields = ( 
        "uuid",
        "created_at",
        "updated_at",
    )

    inlines = [ChoiceInline, ]