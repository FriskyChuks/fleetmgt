from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Car, RideServiceClass, CarOwnerDriverRegister
from .forms import CarOwnersDriversForm


def car_class_view(request, id):
    car_class = Car.objects.filter(service_class_id=id,active=True)
    # car_executive = RideServiceClass.objects.get(id=1)
    # car_luxury = RideServiceClass.objects.get(service_class=2,active=True)
    # car_comfort = RideServiceClass.objects.get(service_class=3,active=True)
    print("class is:")

    template = 'cars/service_class_list.html'
    context = {"car_class":car_class}
    return render(request, template, context)


def car_list_view(request):
    cars = Car.objects.filter(active=True)
    template = 'cars/car_list.html'
    context = {"cars":cars}
    return render(request, template, context)


def car_detail_view(request, id):
    car = Car.objects.get(id=id, active=True)
    template = 'cars/car_detail.html'
    context = {"car":car}
    return render(request, template, context)


def car_owners_and_drivers_view(request):
    user = request.user
    find_user = CarOwnerDriverRegister.objects.filter(user=user)
    msg = ''
    captured_msg = "You are already captured!"
    form = CarOwnersDriversForm(request.POST or None)
    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.user_id = request.user.id
        form_obj.save()
        form = CarOwnersDriversForm()
        msg = 'Your booking is Successful'
    
    template = 'cars/owners_drivers.html'
    context = {"form":form, "find_user":find_user, "msg":msg, "captured_msg":captured_msg}
    return render(request, template, context)
