# apps/news/crud.py
from django.shortcuts import get_object_or_404
from apps.news.models import Post, Event, Survey, Question, QuestionOption, Submission
from apps.news.serializers import (
    PostSerializer,
    EventSerializer,
    SurveySerializer,
    QuestionSerializer,
    QuestionOptionSerializer,
    SubmissionSerializer,
)
from rest_framework.response import Response
from rest_framework import status


# ---------- POST ----------
def create_post(data):
    serializer = PostSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def list_posts():
    posts = Post.objects.all()
    return PostSerializer(posts, many=True).data


def get_post(pk):
    post = get_object_or_404(Post, pk=pk)
    return PostSerializer(post).data


def update_post(pk, data):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_post(pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return {"message": "Post deleted"}


# ---------- EVENT ----------
def create_event(data):
    serializer = EventSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def list_events():
    events = Event.objects.all()
    return EventSerializer(events, many=True).data


def get_event(pk):
    event = get_object_or_404(Event, pk=pk)
    return EventSerializer(event).data


def update_event(pk, data):
    event = get_object_or_404(Event, pk=pk)
    serializer = EventSerializer(event, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_event(pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return {"message": "Event deleted"}


# ---------- SURVEY ----------
def create_survey(data):
    serializer = SurveySerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def list_surveys():
    surveys = Survey.objects.all()
    return SurveySerializer(surveys, many=True).data


def get_survey(pk):
    survey = get_object_or_404(Survey, pk=pk)
    return SurveySerializer(survey).data


def update_survey(pk, data):
    survey = get_object_or_404(Survey, pk=pk)
    serializer = SurveySerializer(survey, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_survey(pk):
    survey = get_object_or_404(Survey, pk=pk)
    survey.delete()
    return {"message": "Survey deleted"}


# ---------- QUESTION ----------
def create_question(data):
    serializer = QuestionSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def list_questions():
    questions = Question.objects.all()
    return QuestionSerializer(questions, many=True).data


def get_question(pk):
    question = get_object_or_404(Question, pk=pk)
    return QuestionSerializer(question).data


def update_question(pk, data):
    question = get_object_or_404(Question, pk=pk)
    serializer = QuestionSerializer(question, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_question(pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return {"message": "Question deleted"}


# ---------- QUESTION OPTION ----------
def create_question_option(data):
    serializer = QuestionOptionSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def list_question_options():
    options = QuestionOption.objects.all()
    return QuestionOptionSerializer(options, many=True).data


def get_question_option(pk):
    option = get_object_or_404(QuestionOption, pk=pk)
    return QuestionOptionSerializer(option).data


def update_question_option(pk, data):
    option = get_object_or_404(QuestionOption, pk=pk)
    serializer = QuestionOptionSerializer(option, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_question_option(pk):
    option = get_object_or_404(QuestionOption, pk=pk)
    option.delete()
    return {"message": "QuestionOption deleted"}


# ---------- SUBMISSION ----------
def create_submission(data):
    serializer = SubmissionSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def list_submissions():
    submissions = Submission.objects.all()
    return SubmissionSerializer(submissions, many=True).data


def get_submission(pk):
    submission = get_object_or_404(Submission, pk=pk)
    return SubmissionSerializer(submission).data


def update_submission(pk, data):
    submission = get_object_or_404(Submission, pk=pk)
    serializer = SubmissionSerializer(submission, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def delete_submission(pk):
    submission = get_object_or_404(Submission, pk=pk)
    submission.delete()
    return {"message": "Submission deleted"}
