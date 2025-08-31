from rest_framework import serializers
from apps.courses.models import Webinar
from apps.courses.serializers.category import CategorySerializer


class WebinarSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Webinar
        fields = [
            "id",
            "title",
            "description",
            "price",
            "card",
            "category",
            "author",
            "datetime",
            "rating",
            "created_at",
            "updated_at",
        ]
