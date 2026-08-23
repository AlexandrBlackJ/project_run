from rest_framework import serializers
from app_run.models import Run


class RunSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с данными модели Run"""
    class Meta:
        model = Run
        fields = '__all__'
