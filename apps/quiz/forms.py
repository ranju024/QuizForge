from django import forms

from apps.quiz.models import Choice

class AnswerForm(forms.Form):
    def __init__(self, *args, question=None, **kwargs):
        super().__init__(*args, **kwargs)

        if question is None:
            return
        
        choices = question.choices.all()
        if question.question_type == "single_choice":
            self.fields["choices"] = forms.ModelChoiceField(
                queryset=choices,
                widget=forms.RadioSelect,
                empty_label=None,
            )
        else:
            self.fields["choices"] = forms.ModelMultipleChoiceField(
                queryset=choices,
                widget=forms.CheckboxSelectMultiple,
            )