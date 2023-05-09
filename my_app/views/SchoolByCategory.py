from rest_framework.generics import ListAPIView

from my_app.models import School
from my_app.serializers import SchoolSerializer


class SchoolByCategory(ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = School.objects.filter(categories_id=category_id)
        return queryset
