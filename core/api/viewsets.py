from rest_framework.viewsets import ModelViewSet
from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer