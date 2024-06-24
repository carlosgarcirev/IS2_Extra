from django.shortcuts import render, HttpResponse
from relecloud import models
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
#def index(request):
#    return HttpResponse('Hello, World!')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

class DestinationsDetailView( generic.DetailView):
    model = models.Destination
    template_name = 'destination_detail.html'
    context_object_name = 'destination'

class CruisesDetailView( generic.DetailView):
    model = models.Cruise
    template_name = 'cruise_detail.html'
    context_object_name = 'cruise'

class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    model = models.InfoRequest
    template_name = 'info_request_create.html'
    fields = ['name', 'email', 'cruise', 'notes']
    success_url = reverse_lazy('index')
    success_message = 'Thank you, %(name)s | We will email you when we have more information about %(cruise)s|'

