from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<uuid:pk>/", views.UserDetailView.as_view()),
    path("users/intitution/", views.UserListInstitutionView.as_view()),
    path("users/volunteers/", views.UserListVolunteersView.as_view()),
    #    path(
    #       "users/<uuid:pk>/campaigns_projects/<uuid:pk>",
    #       views.UserVoluntaryCampaignsProjectsView.as_view(),
    #  ),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
