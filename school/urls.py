from django.urls import path, include
from . import views

from school.views import studentView

urlpatterns = [
    path("sv/",studentView.as_view()),
]
