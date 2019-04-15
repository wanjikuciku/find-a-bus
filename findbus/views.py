from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category,Bus,Profile

# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    return render(request,'index.html')

def search_category(request):
    
    if 'category' in request.GET and request.GET["category"]:
        search_term = (request.GET.get('category')).title()
        searched_buses = Bus.search_by_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{'message':message,'buses':searched_buses})

    else:
        message = "you havent searched for any category"
        return render (request,'search.html',{'message':message})



def my_profile(request):
    user = request.user
    return render(request, "index.html", {"user":user, "current_user":request.user})

def message(request):
    user = request.user
    return render(request, "message.html")