from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('payment/', views.payment, name='payment'),
    path('mpesa_payment/', views.mpesa_payment, name='mpesa_payment'),
    path('grammarly_page/', views.grammarly_page, name='grammarly_page'),



]
