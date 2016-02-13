from django.shortcuts import render
from .helper import filter_place_id, build_api_url, get_hotel_data, build_api_url2
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html', {'a':'a'})

def get_details(request):
    url = request.GET["url"]
    date = request.GET["date"]
    night = "1" if "night" not in request.GET else request.GET["night"]
    currency =  "USD" if "currency" not in request.GET else request.GET["currency"]
    adult =  "1" if "traveler" not in request.GET else request.GET["traveler"]
    room =  "1" if "room" not in request.GET else request.GET["room"]
    place_id = filter_place_id(url)
    api_url = build_api_url(place_id, date, night=night, currency=currency, adult=adult, room=room)
    api_url2 = build_api_url2(place_id, date, night=night, currency=currency, adult=adult, room=room)
    hotel_data = get_hotel_data(api_url, api_url2)
    return HttpResponse(hotel_data)
