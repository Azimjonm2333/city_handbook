from rest_framework.generics import ListAPIView

from my_app.models import School
from my_app.serializers import SchoolSerializer


class SchoolByAddressSearch(ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = School.objects.all()
        search_query = self.kwargs.get('address', None)
        if search_query is not None:
            queryset = queryset.filter(address__icontains=search_query)
        return queryset