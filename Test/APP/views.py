from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def landing_page(request):
    return render(request, 'APP/landing_page.html')

def grammarly_page(request):
    # Your view logic here
    return render(request, 'APP/grammarly_page.html')

def contact(request):
    return render(request, 'APP/contact.html')

def services(request):
    return render(request, 'APP/services.html')

def about(request):
    return render(request, 'APP/about.html')

def register(request):
    if request.method == 'POST':
        # Process registration form here
        
        # Redirect to the login page after successful registration
        return HttpResponseRedirect(reverse('login'))
    else:
        # Handle GET request for the registration form
        return render(request, 'APP/register.html')
    

from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        # Process login form here
        
        # Redirect to a dashboard or profile page after successful login
        return redirect('services')  # Replace 'dashboard' with your desired URL name
    else:
        # Handle GET request for the login form
        return render(request, 'APP/login.html')

from django.shortcuts import render, redirect

def payment(request):
    if request.method == 'POST':
        # In a real scenario, you would handle payment processing here
        # For this example, we'll simulate a successful payment
        amount = request.POST.get('amount')
        context = {'amount': amount}
        return render(request, context)
    
    return render(request, 'APP/payment.html')


import requests
from django.shortcuts import render
from django.http import JsonResponse
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

def mpesa_payment(request):
    # API credentials
    consumer_key = 'TvtG0SBNa4sAC7h82gAOA83N8OPBfgPJ'
    consumer_secret = 'Plxs0RV9g24InOWL'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    # Payment request data (customize this as needed)
    payment_data = {
        'BusinessShortCode': '9886465',
        'Amount': '10',  # The payment amount
        'PartyA': '254700612956',  # Customer's phone number
        'PartyB': '9886465',
        'PhoneNumber': '254700612956',  # Customer's phone number
         "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/", # Callback URL for notifications
        'AccountReference': 'lucyp',
        'TransactionDesc': 'Payment for goods/services',
    }

    # Construct the API request URL
    request_url = 'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

    # Set up authorization header
    auth = 'Bearer ' + requests.get_access_token(consumer_key, consumer_secret)

    # Make the API request
    response = requests.post(request_url, json=payment_data, headers={'Authorization': auth})

    # Handle the API response
    if response.status_code == 200:
        # Payment request successful
        response_data = response.json()
        return JsonResponse(response_data)
    else:
        # Payment request failed
        error_data = response.json()
        return JsonResponse({'error': error_data})
