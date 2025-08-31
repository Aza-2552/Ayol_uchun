from rest_framework import serializers
from apps.courses.models import Course
from apps.courses.serializers.category import CategorySerializer


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "price",
            "card",
            "category",
            "author",
            "rating",
            "created_at",
            "updated_at",
        ]
