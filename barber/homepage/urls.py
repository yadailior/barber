from django.urls import path
from . import views

urlpatterns = [
    path('',views.start,name='home')
    
]

app_name='homepage'