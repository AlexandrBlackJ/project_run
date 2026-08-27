from rest_framework import serializers
from app_run.models import Run
from django.contrib.auth.models import User


class RunSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с данными модели Run"""
    class Meta:
        model = Run
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения данных пользователей"""
    type = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'date_joined', 'username', 'first_name', 'last_name', 'type']

    def get_type(self, obj):
        if obj.is_staff == True:
            return 'couch'
        elif obj.is_staff == False:
            return 'runner'
        else:
            return 'None'