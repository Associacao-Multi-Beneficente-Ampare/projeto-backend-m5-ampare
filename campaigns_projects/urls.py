from django.urls import path
from . import views


urlpatterns = [
    path("campaigns_projects/", views.CampaignsProjectsView.as_view()),
]