from django.shortcuts import render


# Create your views here.

def start(request):
    return render(request,'homepage/home_page.html')