from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from myapplication import views
urlpatterns = [
    path("",views.index, name='myapplication'),
    path("index",views.index),
    path("aboutus",views.aboutus, name='aboutus'),
    path("contact",views.contact, name='contact'),
    path('services',views.services,),
    path('owner',views.owner),
    path('buy',views.buy)
]