from rest_framework import serializers
from apps.news.models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ("id", "user", "question", "chosen_option", "text_answer", "created_at", "updated_at")
