from rest_framework import serializers
from apps.news.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "card",
            "datetime",
            "location_name",
            "longitude",
            "latitude",
            "created_at",
            "updated_at",
        )
