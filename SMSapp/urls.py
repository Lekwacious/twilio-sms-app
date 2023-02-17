from django.urls import path                                                                                                                                                         
from . import views

urlpatterns = [ 
    path(r'broadcast', views.broadcast_sms, name="default"),
]