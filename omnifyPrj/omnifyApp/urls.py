
from django.urls import path
from . import views

urlpatterns = [
    path('fitnessapi-fitness/', views.FitnessAPIView.as_view(), name='fitness'),
    path('bookingapi-booking/', views.BookingAPIView.as_view(), name='booking'),
]