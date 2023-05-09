from rest_framework.generics import ListAPIView

from my_app.models import School
from my_app.serializers import SchoolSerializer


class SchoolByTown(ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        category_id = self.kwargs['town_id']
        queryset = School.objects.filter(town_id=category_id)
        return queryset
