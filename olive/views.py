from django.shortcuts import render
from .helper import filter_place_id, build_api_url, get_hotel_data
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html', {'a':'a'})

def get_details(request):
    url = request.GET["url"]
    date = request.GET["date"]
    place_id = filter_place_id(url)
    api_url = build_api_url(place_id, date)
    hotel_data = get_hotel_data(api_url)
    return HttpResponse(hotel_data)
