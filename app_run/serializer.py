from django.db import models
from rest_framework import serializers
from app_run.models import Run


class Run_Serializers(serializers.Serializer):
    class Meta:
        model = Run
        fields = ['created_at', 'athlete', 'comment']
