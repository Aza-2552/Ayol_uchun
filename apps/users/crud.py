from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from apps.users.models import User, Interest
from apps.users.serializers import UserSerializer


# ---------- CREATE ----------
def create_user(data: dict) -> User:
    """Создать пользователя"""
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return user


# ---------- READ ----------
def get_user_by_id(user_id: int) -> User:
    """Получить пользователя по ID"""
    return get_object_or_404(User, id=user_id, is_deleted=False)


def list_users() -> list[User]:
    """Получить список всех активных пользователей"""
    return User.objects.filter(is_deleted=False)


# ---------- UPDATE ----------
def update_user(user_id: int, data: dict) -> User:
    """Обновить данные пользователя"""
    user = get_user_by_id(user_id)
    serializer = UserSerializer(user, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return user


# ---------- DELETE ----------
def delete_user(user_id: int, reason: str | None = None) -> None:
    """Мягкое удаление (soft delete) пользователя"""
    user = get_user_by_id(user_id)
    user.reason_delete_str = reason or "Deleted by user"
    user.delete_account()


# ---------- EXTRA ----------
def add_interest_to_user(user_id: int, interest_id: int) -> User:
    """Добавить интерес пользователю"""
    user = get_user_by_id(user_id)
    interest = get_object_or_404(Interest, id=interest_id)
    user.interests.add(interest)
    return user


def remove_interest_from_user(user_id: int, interest_id: int) -> User:
    """Удалить интерес у пользователя"""
    user = get_user_by_id(user_id)
    interest = get_object_or_404(Interest, id=interest_id)
    user.interests.remove(interest)
    return user
