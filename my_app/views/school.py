from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from my_app.models import School
from my_app.serializers import SchoolSerializer, SchoolCreateSerializer


class SchoolViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return SchoolCreateSerializer
        return SchoolSerializer