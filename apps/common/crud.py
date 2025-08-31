# apps/common/crud.py
from django.shortcuts import get_object_or_404
from apps.common.models import VersionHistory, FrontendTranslation


# -------------------- VERSION HISTORY --------------------
def create_version(version: str, required: bool = True):
    """Создать запись версии"""
    return VersionHistory.objects.create(version=version, required=required)


def get_version(version_id: int):
    """Получить версию по ID"""
    return get_object_or_404(VersionHistory, id=version_id)


def update_version(version_id: int, **kwargs):
    """Обновить поля версии"""
    version_obj = get_object_or_404(VersionHistory, id=version_id)
    for key, value in kwargs.items():
        setattr(version_obj, key, value)
    version_obj.save()
    return version_obj


def delete_version(version_id: int):
    """Удалить запись версии"""
    version_obj = get_object_or_404(VersionHistory, id=version_id)
    version_obj.delete()
    return True


# -------------------- FRONTEND TRANSLATION --------------------
def create_translation(key: str, text: str):
    """Создать перевод"""
    return FrontendTranslation.objects.create(key=key, text=text)


def get_translation(translation_id: int):
    """Получить перевод по ID"""
    return get_object_or_404(FrontendTranslation, id=translation_id)


def update_translation(translation_id: int, **kwargs):
    """Обновить перевод"""
    translation = get_object_or_404(FrontendTranslation, id=translation_id)
    for key, value in kwargs.items():
        setattr(translation, key, value)
    translation.save()
    return translation


def delete_translation(translation_id: int):
    """Удалить перевод"""
    translation = get_object_or_404(FrontendTranslation, id=translation_id)
    translation.delete()
    return True
