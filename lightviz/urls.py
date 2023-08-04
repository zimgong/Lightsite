from django.urls import path

from . import views

app_name = "lightviz"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("to_third/", views.generic.RedirectView.as_view(url="10.10.10.36:5151"), name="to_third"),
]