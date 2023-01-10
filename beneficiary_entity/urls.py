from django.urls import path
from . import views


urlpatterns = [
    path("beneficiary_entity/", views.BeneficiaryEntityView.as_view()),
    path("beneficiary_entity/<uuid:pk>/", views.BeneficiaryEntityView.as_view()),
]
