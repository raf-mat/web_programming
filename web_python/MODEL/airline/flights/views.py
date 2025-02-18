from django.shortcuts import render

from .models import Flight, Airport
# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

#
def flight(request, flight_id):
     #get me the flight whose id or pk (primary key)= flight_id
    flight = Flight.objects.get(pk=flight_id)
    return render (request, "flights/flight.html", {
        "flight":flight,
        #passengers is the related_name of flights variable into Passenger model
        "passengers": flight.passengers.all()
    })