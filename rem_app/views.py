from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from .serializers import ReminderSerializer
from .services import ReminderService

class ReminderCreateView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            reminder = ReminderService.create_reminder(request.data)
            serializer = ReminderSerializer(reminder)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": f"Unexpected error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

