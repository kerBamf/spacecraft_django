from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('shipwrights/', views.ManufacturerList.as_view(), name="manufacturer_list"),
    path('shipwrights/new/', views.ManufacturerCreate.as_view(), name="manufacturer_create"),
    path('shipwrights/<int:pk>/', views.ManufacturerDetail.as_view(), name="manufacturer_detail"),
    path('shipwrights/<int:pk>/update', views.ManufacturerUpdate.as_view(), name="manufacturer_update"),
    path('shipwrights/<int:pk>/delete', views.ManufacturerDelete.as_view(), name="manufacturer_delete"),
    path('spacecraft/', views.ShipList.as_view(), name="ship_list"),
    path('shipwrights/<int:pk>/spacecraft/new', views.SpacecraftCreate.as_view(), name="spacecraft_create"),
    path('squadrons/<int:pk>/spacecraft/<int:spacecraft_pk>/', views.SquadronSpacecraftAssoc.as_view(), name="squadron_spacecraft_assoc"),
]
