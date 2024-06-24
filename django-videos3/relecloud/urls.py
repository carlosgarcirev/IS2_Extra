## APP (relecloud)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('destinations', views.destinations, name='destinations'),
    path('destination/<int:pk>', views.DestinationsDetailView.as_view(), name='destination-detail'),
    path('cruise/<int:pk>', views.CruisesDetailView.as_view(), name='cruise-detail'),
    path('info-request/', views.InfoRequestCreate.as_view(), name='info-request'),
    
]
