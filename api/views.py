from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import  TodoSerializer,TodoCompleteSerializer
from todo.models import  Todo
from django.utils import timezone

class CreateTodoAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Todo.objects.filter(datecompleted__isnull=False, user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
      return Todo.objects.filter(datecompleted__isnull=False,user=self.request.user)


class TodoUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return Todo.objects.filter(user=self.request.user)


class TodoMarkCompleteAPI(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save(user=self.request.user)