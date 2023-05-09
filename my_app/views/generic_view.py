from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from my_app.models import School
from my_app.serializers import SchoolSerializer, SchoolCreateSerializer, TownSerializer, CategoryFullSerializer

class MySchoolViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):

    permission_classes = [AllowAny]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_queryset(self):
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        self.serializer_class = SchoolCreateSerializer
        return super().create(request, *args, **kwargs) 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        result = serializer.data
        return Response(result)



    @action(detail=True, methods=["get"], url_path="town")
    def town(self, request, *args, **kwargs):
        School = self.get_object()
        result = TownSerializer(School.town)
        return Response(data=result.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], url_path="categories")
    def categories(self, request, *args, **kwargs):
        School = self.get_object()
        self.queryset = School.categories.all()
        self.serializer_class = CategoryFullSerializer
        return super().list(request, *args, **kwargs)

    

    