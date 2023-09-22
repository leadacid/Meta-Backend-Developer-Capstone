from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItem,TableBooking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):
	class Meta: 
            model = MenuItem
            fields = '__all__'
class TableBookingSerializer(serializers.ModelSerializer):
	class Meta: 
            model = TableBooking
            fields = '__all__'
