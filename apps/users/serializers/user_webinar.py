from rest_framework import serializers
from apps.users.models import UserWebinar

class UserWebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWebinar
        fields = ["id", "user", "webinar", "created_at"]
