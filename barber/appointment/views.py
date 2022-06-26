from django.shortcuts import render


# Create your views here.


def queue(request):
    return render(request,'appointment/queue.html')


