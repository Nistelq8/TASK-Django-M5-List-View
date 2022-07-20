from flights.serializers import ListSerializer, BookingSerializer
from .models import Booking, Flight
from rest_framework.generics import ListAPIView

class FlightsListAPIView(ListAPIView):
    queryset  = Flight.objects.all()
    serializer_class = ListSerializer
    
class BookingListAPIView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer