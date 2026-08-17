from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.conf import settings
from .models import Run
from .serializer import Run_Serializers


@api_view(['GET'])
def home_view(request):
    """Страница с описанием компании"""
    contacts = (
        {
            'company_name': settings.COMPANY_NAME,
            'slogan': settings.SLOGAN,
            'contacts': settings.CONTACTS
        }
    )
    return Response(contacts)


class AccountViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с моделью Run"""
    queryset = Run.objects.all()
    serializer_class = Run_Serializers

