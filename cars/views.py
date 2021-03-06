from django.contrib.messages.api import success
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib import messages

from users.models import User

from .models import Car, RideServiceClass, CarOwnerDriverRegister, BankAccountInformation
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

    form = CarOwnersDriversForm(request.POST or None)
    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.user_id = request.user.id
        form_obj.save()
        # messages.success(request, 'Thanks for updating your details; you can continue with other things')
        return redirect("bank_account_info", user_id=user.id)
    
    template = 'cars/owners_drivers.html'
    context = {"form":form}
    return render(request, template, context)


def bank_account_info_view(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        account_name = request.POST.get('account_name')
        account_type = request.POST.get('account_type')
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        form_obj = BankAccountInformation.objects.create(
            user_id = user_id,
            account_name = account_name,
            bank_name = bank_name,
            account_type = account_type,
            account_number = account_number
        )
        form_obj.save()
        messages.success(request, 'Thanks for updating your details; you can continue with other things')
        return redirect("/")
    
    return render(request, 'cars/bank_account_info.html', {"user":user})
