from django.urls import path
from .views import ReminderCreateView,ReminderListView

urlpatterns = [
    path("create-reminder/", ReminderCreateView.as_view(), name="create-a-reminder"),
    path('get-reminders/', ReminderListView.as_view(), name='reminder-list'),
]
