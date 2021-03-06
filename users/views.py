from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages


from cars.models import Car, CarOwnerDriverRegister, BankAccountInformation

from .forms import LoginForm, SignUpForm


def home_view(request):
    cars = Car.objects.all()

    template = 'home.html'
    context = {"cars":cars}
    return render(request, template, context)


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            
            if user is not None:
                login(request, user)
                is_driver = user.is_a_driver
                is_car_owner = user.is_car_owner
                car_owner_driver_profile = CarOwnerDriverRegister.objects.filter(user_id=user.id)
                has_bank_info = BankAccountInformation.objects.filter(user_id=user.id)
                if (is_driver or is_car_owner):
                    if (len(car_owner_driver_profile) <= 0):
                        messages.info(request, 'Kindly update your record before proceeding, thanks!')
                        return redirect("/cars/car_owners_and_drivers")
                    elif not has_bank_info:
                        messages.info(request, "Kindly update your bank details before proceeding, thanks!")
                        return redirect("bank_account_info", user_id=user.id)
                    else:
                        if "next" in request.POST:
                            return redirect(request.POST.get('next'))
                        else:
                            return redirect("/")
                else:
                    if "next" in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Wrong login credentials!'    

    return render(request, "users/login.html", {"form": form, "msg" : msg})



def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)

            msg     = 'User created successfully! - please <a href="/">login</a>.'
            success = True
            
            return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "users/register.html", {"form": form, "msg" : msg, "success" : success })


def logout_view(request):
    logout(request)
    # messages.success(request, "Sad to see you leave! See you soon please!")
    return HttpResponseRedirect('%s'%(reverse("home")))
