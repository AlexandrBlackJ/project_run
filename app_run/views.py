from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.conf import settings
from .models import Run
from .serializer import RunSerializer


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


class RunViewSet(viewsets.ModelViewSet):
    """ViewSet для работы url 'api/runs', обрабатывает данные из модели Run"""
    queryset = Run.objects.all()
    serializer_class = RunSerializer
