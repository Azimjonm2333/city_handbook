from rest_framework.generics import ListAPIView

from my_app.models import Place
from my_app.serializers import PlaceSerializer


class PlaceByCity(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        category_id = self.kwargs['city_id']
        queryset = Place.objects.filter(city_id=category_id)
        return queryset
