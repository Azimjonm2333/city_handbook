from rest_framework.generics import ListAPIView

from my_app.models import School
from my_app.serializers import SchoolSerializer


class SchoolByNameSearch(ListAPIView):
    serializer_class = SchoolSerializer
    

    def get_queryset(self):
        queryset = School.objects.all()
        search_query = self.kwargs.get('name', None)
        if search_query is not None:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset