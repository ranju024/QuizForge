from django.urls import path
from .views import DashboardView, MyAttemptsView

app_name = "dashboard"

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
    path("my-attempts/", MyAttemptsView.as_view(), name="attempts", ),
]