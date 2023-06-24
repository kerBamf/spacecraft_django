from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('shipwrights', views.ManufacturerList.as_view(), name="manufacturer_list"),
    path('shipwrights/new/', views.ManufacturerCreate.as_view(), name="manufacturer_create"),
    path('shipwrights/<int:pk>/', views.ManufacturerDetail.as_view(), name="manufacturer_detail"),
    path('spacecraft', views.ShipList.as_view(), name="ship_list"),
]