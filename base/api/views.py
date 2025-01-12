from rest_framework import viewsets, permissions
from .serializer import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = TaskSerializer.Meta.model.objects.all()
    permission_classes = [permissions.IsAuthenticated]

