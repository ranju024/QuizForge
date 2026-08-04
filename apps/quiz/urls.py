from django.urls import path
from apps.quiz.views import(
    QuizListView, QuizDetailView, StartQuizView, TakeQuizView, ResultView
)

app_name = "quiz"
urlpatterns = [
    path("", QuizListView.as_view(), name="list"),
    path("<int:pk>/", QuizDetailView.as_view(), name="detail"),
    path("<int:pk>/start/", StartQuizView.as_view(), name="start"),
    path("attempt/<int:attempt_id>/question/<int:question_no>/", TakeQuizView.as_view(), name="take"),
    path("attempt/<int:pk>/result", ResultView.as_view(), name="result"), 
]
