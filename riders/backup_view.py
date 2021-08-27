from django.shortcuts import render
import geoip2.database
from geopy.geocoders import Nominatim

from .models import Ride
from .forms import BookRideForm
from .utils import get_geo


def book_a_ride_view(request):
    form = BookRideForm(request.POST or None)
    geolocator = Nominatim(user_agent="riders")

    ip = '72.14.207.99'
    country, city, lat, lon = get_geo(ip)
    print('country:', country)
    print('city:', city)
    print('lat:', lat)
    print('lon:', lon)

    msg = ""
    if form.is_valid():
        new_form = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)
        print(destination)
        d_lat = destination.latitude
        d_lon = destination.longitude

        new_form.rider_id = request.user.id
        # new_form.save()
        form = BookRideForm()
        msg = 'Your booking is Successful'
   
    template = 'riders/book_ride.html'
    context = {"form":form, "msg":msg}
    return render(request, template, context)


def riders_list_view(request):
    riders = Ride.objects.filter(status=1)
    print(riders)

    template = 'riders/riders_list.html'
    context = {"riders":riders}
    return render(request, template, context)


