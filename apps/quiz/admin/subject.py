from django.contrib import admin

from apps.quiz.models import Subject

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "theme",
        "is_active",
        "created_at",
    )
    list_filter = (
        "is_active",
        "theme",
    )
    search_fields = (
        "name",
        "description",
    )
    # list_per_page = 20
    ordering = ("name",)

    readonly_fields = (
        "uuid",
        "created_at",
        "updated_at",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }