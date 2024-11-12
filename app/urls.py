from django.urls import path
from app import views


urlpatterns=[path('home/',views.home),
             path('login/',views.log_users,name='login'),
             path('eye/',views.eyeglass,name='eye'),
             path('si/', views.si),
             path('track/',views.track),
             path('power/',views.pwr,name='pwr'),
             path('sn/',views.sun),
             path('power/',views.po),
             path('lo/',views.lo,name='lo'),
             path('sunglasses/',views.sun,name='sun'),
             path('shop/',views.detail,name='shop'),
             path('profile/',views.profile),
             path('logout/',views.logout_users,name='logout'),
             path('round/',views.round,name='round'),
             path('johnj/',views.john,name='john'),
             path('cart/',views.ct,name='ct'),
             path('wishlist/',views.wish,name='wish'),
             path('contact/',views.contaact,name='contact'),
             path('remove/',views.remove,name='remove')
             ]  