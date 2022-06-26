from django.urls import path
from . import views


urlpatterns = [
    path('',views.queue,name='queue')
    
]

app_name='appointment'