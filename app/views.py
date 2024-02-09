from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Place, Package, ContactRequest

# Create your views here.

def index(request):
    packages = Package.objects.all().values()
    context = {
        'packages': packages,
    }
    return render(request, 'index.html', context)

def search(request):
    if request.method == "GET":
        return redirect("home_view")
    else:
        packagename = request.POST.get('packagename')
        people = int(request.POST.get('people'))
        cancelable = request.POST.get('cancelable')
        if cancelable is None:
            cancelable = 0
        else: 
            cancelable = 1
        
        packages = Package.objects.filter(name=packagename).filter(max_travelers__lte=people).filter(is_cancelable=cancelable)
        # placeList = []
        # for (package in packages) {
        #     places = package.places.all()
        #     for (place in places) {
        #         placeIDList += place.placeID
        #     }
        # }
        # images = PlaceImage.objects.filter(place__in=places.placeID)
        context = {
            'packages': packages,
            'searchquery': packagename,
        }
        return render(request, 'searchresult.html', context)

def services(request):
    return render(request,'services.html',{})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        c = ContactRequest()
        contact = ContactRequest(requestID=c.getUniqueRequestID(), first_name=first_name,last_name=last_name,email=email)
        contact.save()
        return redirect('home_view')
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html',{})

@login_required
def packageDetail(request, packageID):
    package = get_object_or_404(Package, pk=packageID)
    context = {
        'package': package,
    }
    return render(request,'package_detail.html',context)

def get_packages(request):
    packages = Package.objects.all()
    context = {
        'packages': packages,
    }
    return render(request,'packages.html',context)

@login_required
def book(request):
    return render(request,'book.html',{})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_view")
        else:
            print(email, "Mahin")
            messages.error(request, "Invalid username or password!")
    return render(request,'login.html',{})

def user_signup(request):
    if request.method == 'POST':
        user_registration_form = UserRegistrationForm(request.POST)
        if user_registration_form.is_valid():
            user_registration_form.save()
            email = user_registration_form.cleaned_data['email']
            password = user_registration_form.cleaned_data['password1']
            user = authenticate(username=email, password=password)
            login(request, user)
            messages.success(request, "Registered Successfully.")
            return redirect('home_view')
    else:
        user_registration_form = UserRegistrationForm()
    return render(request,'signup.html',{"form": user_registration_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home_view')

@login_required
def editprofile(request):
    return render(request,'editprofile.html',{})