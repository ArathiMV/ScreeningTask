from django.db import models

# Model for Remind-Me-Later
class Reminder(models.Model):
    REM_TYPES = [("SMS","SMS"),("EMAIL","Email")]
    message = models.TextField(help_text="Reminder message text")
    reminder_type = models.CharField(max_length=10, choices=REM_TYPES, default="EMAIL")
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        f"{self.reminder_type} - {self.message[:20]} ({self.date} {self.time})"

