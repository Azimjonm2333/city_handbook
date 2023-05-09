from django.urls import path, include
from rest_framework import routers

from my_app.views import PlaceViewSet, PlaceByCategory, PlaceByCity, PlaceByAddressSearch, PlaceByNameSearch

router = routers.DefaultRouter()
router.register("places", PlaceViewSet, "places")

urlpatterns = [
    path('', include(router.urls)),

    path('places/category/<int:category_id>', PlaceByCategory.as_view()),
    path('places/city/<int:city_id>', PlaceByCity.as_view()),
    
    path('places/address/<str:address>', PlaceByAddressSearch.as_view()),
    path('places/name/<str:name>', PlaceByNameSearch.as_view()),
]

