from django.shortcuts import render
from .helper import HotelScraper
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html', {'a':'a'})

def get_details(request):
    url = request.GET["url"]
    date = request.GET["date"]
    adult = request.GET["traveler"]
    night = request.GET["night"]
    room = request.GET["room"]
    hotel_data = HotelScraper(url, date, adult, night, room).get_data()
    return HttpResponse(hotel_data)
