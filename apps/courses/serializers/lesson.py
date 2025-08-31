from rest_framework import serializers
from apps.courses.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "module",
            "title",
            "description",
            "file",
            "duration",
            "created_at",
            "updated_at",
        ]
