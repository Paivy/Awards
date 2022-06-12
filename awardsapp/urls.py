from django.urls import path
from . import views

urlpatterns = [
    # int: numbers
    # str: strings
    # path: whole urls/
    # slugs: hyphen-and_underscores_stuff
    #UUID: universally unique identifiers

     path('',views.home, name="home"),
    #  path('add_site',views.add_site,name="add_site"),
]