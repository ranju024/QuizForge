from django.views.generic import ListView, DetailView

from apps.quiz.models import Quiz

class QuizListView(ListView):
    model = Quiz
    template_name = "quiz/quiz_list.html"
    context_object_name = "quizzes"

    def get_queryset(self):
        return Quiz.objects.filter(is_active=True,)
    
class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quiz/quiz_detail.html"
    context_object_name = "quiz"
    