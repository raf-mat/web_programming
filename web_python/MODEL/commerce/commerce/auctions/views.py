from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import AuctionListing
from .forms import NewListing

from .models import User


def index(request):
    return render(request, "auctions/index.html", {
        "auctionlisting": AuctionListing.objects.all(),
    })

def create(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the
        form = NewListing(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # Create a new Auction instance using the data
            new_listing = AuctionListing(
            title=form.cleaned_data['title'], 
            category=form.cleaned_data['category'],
            description=form.cleaned_data['description'],
            starting_bid=form.cleaned_data['starting_bid'],
            image=form.cleaned_data['image'],
            )
            # Save the article to the database
            new_listing.save()

            # return index.html updated:
            return render(request, "auctions/index.html", {
        "auctionlisting": AuctionListing.objects.all(),
        })
    
        # If the form was invalid send the user back to fix it
        else:
            return render(request, "auctions/create.html")
        
    return render(request, "auctions/create.html",{
        "form": NewListing()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
