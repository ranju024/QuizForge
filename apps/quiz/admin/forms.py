from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from apps.quiz.services.question_service import QuestionService

class ChoiceInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        choices = []

        for form in self.forms:
            if not hasattr(form, "cleaned_data"):
                continue
            if form.cleaned_data.get("DELETE", False):
                continue
            if not form.cleaned_data:
                continue
            choices.append(form.instance)

        QuestionService.validate(
            self.instance, choices,
        )