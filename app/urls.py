from django.contrib import admin
from django.urls import include, path
from app import views
urlpatterns = [
   
    path('api/location',views.get_location),
    path('api/location/<id>',views.get_location),
    path('api/alllocation',views.alllocation)
]
