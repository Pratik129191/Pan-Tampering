from django.urls import path
from . import views

app_name = 'service'


urlpatterns = [
    path('hello/', views.say_hello, name='hello'),
    path('pan/', views.pan_details, name='detail'),
    path('pan/<id>/', views.pan_tampered, name='check'),
]

