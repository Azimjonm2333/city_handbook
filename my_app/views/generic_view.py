from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from my_app.models import Place
from my_app.serializers import PlaceSerializer, PlaceCreateSerializer, CitySerializer, CategoryFullSerializer

class MyPlaceViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):

    permission_classes = [AllowAny]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        self.serializer_class = PlaceCreateSerializer
        return super().create(request, *args, **kwargs) 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        result = serializer.data
        return Response(result)



    @action(detail=True, methods=["get"], url_path="town")
    def town(self, request, *args, **kwargs):
        Place = self.get_object()
        result = CitySerializer(Place.town)
        return Response(data=result.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], url_path="categories")
    def categories(self, request, *args, **kwargs):
        Place = self.get_object()
        self.queryset = Place.categories.all()
        self.serializer_class = CategoryFullSerializer
        return super().list(request, *args, **kwargs)

    

    