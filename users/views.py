from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


#from drf_spectacular.utils import extend_schema

from .serializers import UserSerializer
#from .permissions import IsAccountOwner
from .models import User



class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
   # authentication_classes = [JWTAuthentication]
   # permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class ListUserVoluntaryView(generics.ListAPIView):


    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        route_parameter = self.request.GET.get("is_superuser") 

        if route_parameter: 
        
            queryset = User.objects.filter(is_superuser=True)
            return queryset 
        
        return super().get_queryset()