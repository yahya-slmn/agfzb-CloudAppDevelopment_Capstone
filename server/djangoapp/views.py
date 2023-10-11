from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    return render(request, 'djangoapp/about.html')

# ...


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other page after successful login
            return redirect('success_view_name')
        else:
            # Handle invalid login credentials, e.g., display an error message
            return render(request, 'djangoapp/login.html', {'error_message': 'Invalid login credentials'})
    else:
        # Render the login form
        return render(request, 'djangoapp/login.html')


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return render(request, 'djangoapp/logout.html')

# Create a `registration_request` view to handle sign up request
def signup(request):
    if request.method == 'POST':
        # Get data from the registration form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Authenticate and log in the new user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other page after successful registration and login
            return redirect('success_view_name')
    
    # Render the registration form page (GET request)
    return render(request, 'djangoapp/registration.html')

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

