from django.urls import path, include
from rest_framework import routers

from my_app.views import SchoolViewSet, SchoolByCategory, SchoolByTown, SchoolByAddressSearch, SchoolByNameSearch

router = routers.DefaultRouter()
router.register("schools", SchoolViewSet, "schools")

urlpatterns = [
    path('', include(router.urls)),

    path('schools/category/<int:category_id>', SchoolByCategory.as_view()),
    path('schools/town/<int:town_id>', SchoolByTown.as_view()),
    
    path('schools/address/<str:address>', SchoolByAddressSearch.as_view()),
    path('schools/name/<str:name>', SchoolByNameSearch.as_view()),
]

