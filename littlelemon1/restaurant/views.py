from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from .serializers import UserSerializer, MenuItemSerializer,TableBookingSerializer
from .models import MenuItem
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import TableBooking



# Create your views here.

@api_view()
@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})


def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CreateBookingView(generics.ListCreateAPIView):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer

class SingleBookingView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer