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
    path('forgot_password/', views.forgot_password, name='forgot_password'),

    path('grammarly_page/', views.grammarly_page, name='grammarly_page'),

]


from .views import SubmitView, CheckTransaction, ConfirmView, CheckTransactionOnline

mpesa_urls = [
    path('submit/', SubmitView.as_view(), name='submit'),
    path('confirm/', ConfirmView.as_view(), name='confirm'),
    path('check-online/', CheckTransactionOnline.as_view(), name='confirm-online'),
    path('check-transaction/', CheckTransaction.as_view(), name='check_transaction'),
]