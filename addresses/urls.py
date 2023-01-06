from django.urls import path, include 
from . import views

urlpatterns = [
    path("addresses/", views.AddressView.as_view())
]