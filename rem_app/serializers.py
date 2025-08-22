from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ["id","message", "date", "time","reminder_type", "created_at","updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]