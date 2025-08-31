from rest_framework import serializers
from apps.users.models import UserCourse

class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ["id", "user", "course", "created_at"]
