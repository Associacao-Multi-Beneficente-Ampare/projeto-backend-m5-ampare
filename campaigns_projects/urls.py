from django.urls import path
from . import views
from beneficiary_entity import views as entity_view

urlpatterns = [
    path("campaigns_projects/", views.CampaignsProjectsView.as_view()),
    path("campaigns_projects/<uuid:pk>/beneficiary_entity/", entity_view.BeneficiaryEntityView.as_view()),
]