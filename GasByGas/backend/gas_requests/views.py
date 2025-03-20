from django.shortcuts import render


def home(request):
    return render(request, 'gas_requests/home.html')   # Make sure home.html exists
