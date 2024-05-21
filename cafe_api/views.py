from .models import Cafe
from .serializers import CafeSerializer
from rest_framework import viewsets

class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer


