from django.shortcuts import render
# from .models import *
# from .forms import SiteForm
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