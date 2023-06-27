from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        'flights': Flights.objects.all()
    })
def flight(request,flight_id):
    flight=Flights.objects.get(id=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "pas":flight.passengers.all()
    })