from django.urls import path

from . views import ListTruck, DetailTruck, TruckItems, TruckItemsBuy , Truckinventory

urlpatterns = [
    path('trucks/', ListTruck.as_view()),
    path('truck/<int:pk>/', DetailTruck.as_view()),
    path('truck/<int:pk>/items/', TruckItems.as_view()),
    path('truck/buy/', TruckItemsBuy.as_view()),
    path('truck/<int:pk>/inventory/', Truckinventory.as_view()),
]

#{"truck": 1, "product" :"ice_cream","id":2}