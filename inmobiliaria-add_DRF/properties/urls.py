from django.urls import path
from .views import PropertyView, update_property, delete_property

urlpatterns = [
    path('properties/', PropertyView, name='property_list'),
    path('property/new/', PropertyView, name='create_property'),
    path('property/edit/<int:id>/', update_property, name='update_property'),
    path('property/delete/<int:id>/', delete_property, name='delete_property'),
]




