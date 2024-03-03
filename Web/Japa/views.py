from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import timedelta
from .models import CustomUser
from .forms import *
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone

# Create your views here.
def index(request):
    restauranter = NyRestaurant.objects.all()
    kategorier = NyKategori.objects.all()
    return render(request, 'index.html', {'user': request.user, 'Restauranter': restauranter, 'Kategorier': kategorier})

@require_POST
def create_bestilling(request):
    if request.method == 'POST':
        data = request.POST



def logout_view(request):
    logout(request)
    return redirect('index')

def restaurant_detail(request, Navn):
    restauranter = get_object_or_404(NyRestaurant, Navn=Navn)
    underkategorier_set = set()
    nytmad_set = set()


    # Assuming NyRestaurant has a Many-to-Many relationship with NyKategori, and NyKategori has a Many-to-Many relationship with NyUnderkategori
    for kategori in restauranter.Kategorier.all():
        for underkategori in kategori.nyunderkategori_set.all():
            underkategorier_set.add(underkategori)

    underkategorier = list(underkategorier_set)

    for underkategori in underkategorier:
        for mad in underkategori.nytmad_set.all():
            nytmad_set.add(mad)

    nytmad = list(nytmad_set)

    return render(request, 'restaurant_detail.html', {'Restauranter': restauranter, 'Underkategorier': underkategorier, 'NytMad': nytmad})

def checkout_view(request, Navn):
    restauranter = get_object_or_404(NyRestaurant, Navn=Navn)
    underkategorier_set = set()
    nytmad_set = set()


    # Assuming NyRestaurant has a Many-to-Many relationship with NyKategori, and NyKategori has a Many-to-Many relationship with NyUnderkategori
    for kategori in restauranter.Kategorier.all():
        for underkategori in kategori.nyunderkategori_set.all():
            underkategorier_set.add(underkategori)

    underkategorier = list(underkategorier_set)

    for underkategori in underkategorier:
        for mad in underkategori.nytmad_set.all():
            nytmad_set.add(mad)

    nytmad = list(nytmad_set)
    return render(request, 'checkout.html', {'user': request.user, 'Restauranter': restauranter, 'Underkategorier': underkategorier, 'NytMad': nytmad})


def manage_view(request):
    restaurant_form = NyRestaurantForm()
    category_form = NyKategoriForm()
    food_form = NytMadForm()
    undercategory_form = NyUnderkategoriForm()

    if request.method == 'POST':
        if 'restaurant_form' in request.POST:
            restaurant_form = NyRestaurantForm(request.POST, request.FILES)
            if restaurant_form.is_valid():
                restaurant_form.save()
                return redirect('manage')  # Redirecting without passing context
        elif 'category_form' in request.POST:
            category_form = NyKategoriForm(request.POST, request.FILES)
            if category_form.is_valid():
                category_form.save()
                return redirect('manage')
        elif 'food_form' in request.POST:
            food_form = NytMadForm(request.POST, request.FILES)
            if food_form.is_valid():
                food_form.save()
                return redirect('manage')
        elif 'undercategory_form' in request.POST:
            undercategory_form = NyUnderkategoriForm(request.POST, request.FILES)
            if undercategory_form.is_valid():
                undercategory_form.save()
                return redirect('manage')

    # If it's not a POST request or form submission failed, render the template with the forms
    return render(request, 'manage.html', {'restaurant_form': restaurant_form,
                                            'category_form': category_form,
                                            'food_form': food_form,
                                            'undercategory_form': undercategory_form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            if remember_me:
                request.session.set_expiry(timedelta(days=14))
            else:
                request.session.set_expiry(0)

            return redirect('index')  # Adjust as per your index/home view
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        address_type = request.POST['address_type']
        door_number = request.POST['door_number']

        # Add validation logic here

        # Creating a new user instance
        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            address_type=address_type,
            door_number=door_number
        )
        user.save()

        messages.success(request, 'Account created successfully')
        return redirect('login')  # Redirect to login page after signup
    return render(request, 'signup.html')

def success_view(request):
    return render(request, 'success.html')