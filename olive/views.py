from django.shortcuts import render
from .helper import HotelScraper
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'index.html', {'a':'a'})

@csrf_exempt
def get_details(request):
    hotel_data = "You're looking good today!"
    if request.method == 'POST':
        import json
        r_data = json.loads(request.body)
        url = r_data["url"]
        date = r_data["date"]
        adult = r_data["traveler"]
        night = r_data["night"]
        room = r_data["room"]
        hotel_data = HotelScraper(url, date, adult, night, room).get_data()
    return HttpResponse(hotel_data)
