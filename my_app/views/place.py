from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from my_app.models import Place
from my_app.serializers import PlaceSerializer, PlaceCreateSerializer


class PlaceViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return PlaceCreateSerializer
        return PlaceSerializer