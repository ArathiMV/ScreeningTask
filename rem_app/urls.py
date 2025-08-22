from django.urls import path
from .views import ReminderCreateView

urlpatterns = [
    path("create-reminder/", ReminderCreateView.as_view(), name="create-a-reminder"),
]
