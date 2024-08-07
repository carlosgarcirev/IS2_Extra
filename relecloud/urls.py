from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('destinations/', views.destinations, name='destinations'),
    path('destination/<int:pk>', views.DestinationDetailView.as_view(), name='destination_detail'),
    path('cruise/<int:pk>', views.CruiseDetailView.as_view(), name='cruise_detail'),
    path('opiniones/', views.opiniones, name='opiniones'),
    path('info_request', views.InfoRequestCreate.as_view(), name='info_request'),
    path('info_request/success', views.info_request_success, name='info_request_success'),
]