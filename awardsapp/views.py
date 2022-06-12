from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request, 'home.html')

# def add_site(request):
#     submitted = False

#     if request.method == 'POST':
#          form = SiteForm(request.POST)
#          if form.is_valid():
#              form.save()
#              return HttpResponseRedirect('/add_site?submitted=True')
#     else:
#         form = SiteForm
#         if 'submitted' in request.GET:
#             submitted = True
#             return render(request, 'add_site.html',
#     {'form':form, 'submitted':submitted})
        

   
#     return render(request, 'events/add_venue.html',
#     {'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
