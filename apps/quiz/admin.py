from django.contrib import admin

from apps.quiz.models import Subject, Topic

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "theme",
        "is_active",
        "created_at",
    )
    # list_filter = (
    #     "is_active",
    #     "theme",
    # )
    search_fields = (
        "name",
        "description",
    )
    # prepopulated_fields = {
    #     "slug": ("name",)
    # }
    # list_per_page = 20
    ordering = ("name",)



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
    # prepopulated_fields = {
    #     "slug": ("name",)
    # }
    autocomplete_fields = (
        "subject",
    )
