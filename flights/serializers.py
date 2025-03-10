from rest_framework import serializers
from .models import Flight, Booking

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id','destination','time']
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight','date','id']