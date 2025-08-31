from rest_framework import serializers
from apps.news.models import Question
from apps.news.serializers.question_option import QuestionOptionSerializer


class QuestionSerializer(serializers.ModelSerializer):
    options = QuestionOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "survey", "title", "type", "file", "options", "created_at", "updated_at")
