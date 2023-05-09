from rest_framework.generics import ListAPIView

from my_app.models import Place
from my_app.serializers import PlaceSerializer


class PlaceByAddressSearch(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        queryset = Place.objects.all()
        search_query = self.kwargs.get('address', None)
        if search_query is not None:
            queryset = queryset.filter(address__icontains=search_query)
        return queryset