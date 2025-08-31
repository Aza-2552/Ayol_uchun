from rest_framework import serializers
from apps.courses.models import Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = [
            "id",
            "course",
            "name",
            "icon",
            "created_at",
            "updated_at",
        ]
