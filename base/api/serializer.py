from rest_framework import serializers
from base.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {"url":{"lookup_fields":"pk"}}
        lookup_field = "pk"