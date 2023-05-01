from django.urls import path

from integration.views import (
    HomeView,
    form_view,
)

urlpatterns = [
    path("", HomeView.as_view()),
    path("form", form_view, name='form'),
]
