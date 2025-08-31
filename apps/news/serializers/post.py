from rest_framework import serializers
from apps.news.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "description", "card", "created_at", "updated_at")
