from rest_framework import serializers
from apps.courses.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "course",
            "webinar",
            "text",
            "rating",
            "created_at",
            "updated_at",
        ]
