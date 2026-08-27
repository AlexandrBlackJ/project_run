from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.conf import settings
from .models import Run
from .serializer import RunSerializer, UserSerializer
from django.contrib.auth.models import User


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
    """ViewSet для работы с url 'api/runs', обрабатывает данные из модели Run"""
    queryset = Run.objects.all()
    serializer_class = RunSerializer


class UserView(viewsets.ReadOnlyModelViewSet):
    """ViewSet для работы с url 'api/users/'"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """Фильтрация пользователей по ролям. Исключение админов из ответа"""
        query = User.objects.filter(is_superuser=False)

        # stuff = self.request.query_params.get('is_staff')
        type = self.request.query_params.get('type')
        if type == 'coach':
            query = query.filter(is_staff=True)
        elif type == 'athlete':
            query = query.filter(is_staff=False)
        return query


    # def get_queryset(self):
    #     """queryset для исключения super_user из ответа"""
    #     queryset = super().get_queryset()
    #     qury = self.queryset.filter(is_superuser=False)
    #     return qury
