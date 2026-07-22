from django.contrib import admin

from apps.quiz.models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "subject",
        "order",
        "is_active",
    )

    list_filter = (
        "subject",
        "is_active",
    )

    search_fields = (
        "name",
        "subject__name",
    )

    ordering = (
        "subject",
        "order",
    )

    autocomplete_fields = (
        "subject",
    )

    readonly_fields = (
        "uuid",
        "created_at",
        "updated_at",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }