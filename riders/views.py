from django.shortcuts import redirect, render
# import geoip2.database
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from django.contrib.auth.decorators import login_required

from .models import Ride
from .forms import BookRideForm
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address


@login_required
def book_a_ride_view(request):
    # Initialise variables
    distance = None
    destination = None

    form = BookRideForm(request.POST or None)
    geolocator = Nominatim(user_agent="riders")

    ip_ = get_ip_address(request)
    
    # ip = '72.14.207.99' # USA
    ip = '23.248.172.255' # NIGERIA
    country, city, lat, lon = get_geo(ip_)
    location = geolocator.geocode(city)

    # FOR CURRENT LOCATION COORDINATES
    location_lat = lat
    location_lon = lon
    pointA = (location_lat, location_lon)
    print('Point A is',pointA)

    # INITIAL FOLIUM MAP
    m = folium.Map(width=800, height=500, location=get_center_coordinates(location_lat, location_lon), zoom_start=1)
    # LOCATION MARKER
    folium.Marker([location_lat, location_lon], tooltip='click here for more', popup=city['city'],
                    icon=folium.Icon(color='purple')).add_to(m)

    msg = ""
    if form.is_valid():
        new_form = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)

        # for DESTINATION COORDINATES
        if not destination:
            # DISTANCE CALCULATION
            distance = 0.00
            new_form.pickup_address = location
            new_form.destination = form.cleaned_data.get('destination')
            new_form.distance = distance
            new_form.rider_id = request.user.id
            new_form.save()
            form = BookRideForm()
            msg = 'Your booking is Successful'
        else:
            destination_lat = destination.latitude
            destination_lon = destination.longitude
            pointB = (destination_lat, destination_lon)
            # DISTANCE CALCULATION
            distance = round(geodesic(pointA, pointB).km, 2)

            # FOLIUM MAP MODIFICATION
            m = folium.Map(width=800, height=500, location=get_center_coordinates(location_lat, location_lon, destination_lat, destination_lon), zoom_start=get_zoom(distance))
            # LOCATION MARKER
            folium.Marker([location_lat, location_lon], tooltip='click here for more', popup=city['city'],
                        icon=folium.Icon(color='purple')).add_to(m)

            # DESTINATION MARKER
            folium.Marker([destination_lat, destination_lon], tooltip='click here for more', popup=destination,
                        icon=folium.Icon(color='red', icon='cloud')).add_to(m)

            # DRAW LINE BETWEEN LOCATION & DESTINATION
            line = folium.PolyLine(locations=[pointA, pointB], weight=2, color='blue')
            m.add_child(line)

            new_form.pickup_address = location
            new_form.destination = destination
            new_form.distance = distance
            new_form.rider_id = request.user.id
            new_form.save()
            form = BookRideForm()
            msg = 'Your booking is Successful'
            # return redirect()
        
    m = m._repr_html_()
   
    template = 'riders/book_ride.html'
    context = {"form":form, 
                "msg":msg,
                "map":m,
                "distance":distance,
                "destination":destination,
                'city':city
            }
    return render(request, template, context)



def riders_list_view(request):
    pending_riders = Ride.objects.filter(status=1)# Pending riders
    active_riders = Ride.objects.filter(status=3)# Active Riders
    # print(riders)

    template = 'riders/riders_list.html'
    context = {"pending_riders":pending_riders, "active_riders":active_riders}
    return render(request, template, context)


