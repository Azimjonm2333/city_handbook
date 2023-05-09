from rest_framework.generics import ListAPIView

from my_app.models import Place
from my_app.serializers import PlaceSerializer


class PlaceByCategory(ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Place.objects.filter(categories_id=category_id)
        return queryset
