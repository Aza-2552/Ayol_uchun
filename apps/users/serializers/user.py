from rest_framework import serializers
from apps.users.models import User, Interest

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ["id", "name"]

class UserSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "phone_number",
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "bio",
            "is_active",
            "is_confirmed",
            "interests",
        ]
        read_only_fields = ["is_active", "is_confirmed"]
