from .models import Reminder
from datetime import datetime, date, time as time_cls
from django.core.exceptions import ValidationError

class ReminderService:

    @staticmethod
    def create_reminder(data: dict) -> Reminder:

        message = data.get("message")
        reminder_type = data.get("reminder_type")
        reminder_date = data.get("date")
        reminder_time = data.get("time")

        if not message:
            raise ValidationError("Message is required.")
        if not reminder_type:
            raise ValidationError("Reminder type is required.")
        if not reminder_date:
            raise ValidationError("Date is required.")
        if not reminder_time:
            raise ValidationError("Time is required.")

        if reminder_type not in dict(Reminder.REM_TYPES):
            raise ValidationError(
                f"Invalid reminder_type '{reminder_type}'. Allowed: {list(dict(Reminder.REM_TYPES).keys())}"
            )
        if isinstance(reminder_date, str):
            try:
                reminder_date = datetime.strptime(reminder_date, "%Y-%m-%d").date()
            except ValueError:
                raise ValidationError("Date must be in YYYY-MM-DD format")
        if reminder_date < date.today():
            raise ValidationError("You cannot set Reminder for a past date")
        if isinstance(reminder_time, str):
            try:
                reminder_time = datetime.strptime(reminder_time, "%H:%M").time()
            except ValueError:
                raise ValidationError("Time must be in HH:MM format")
        reminder = Reminder.objects.create(
            message=message,
            reminder_type=reminder_type,
            date=reminder_date,
            time=reminder_time,
        )
        return reminder
