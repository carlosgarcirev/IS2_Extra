from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from .models import Opinion, Cruise
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', { 'destinations': all_destinations})

def opiniones(request):
    if request.method == "POST":
        title = request.POST.get("title")
        opinion_text = request.POST.get("opinion_text")
        cruise_id = request.POST.get("cruise_id")
        if title and opinion_text and cruise_id:
            cruise = Cruise.objects.get(id=cruise_id)
            Opinion.objects.create(title=title, opinion_text=opinion_text, cruise=cruise)
            return redirect('opiniones')
    
    cruises = Cruise.objects.all().prefetch_related('opinions')
    return render(request, 'opiniones.html', {'cruises': cruises})


class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'

class CruiseDetailView(generic.DetailView):
    template_name = 'cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'

class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'info_request_create.html'
    model = models.InfoRequest
    fields = ['name', 'email', 'cruise', 'notes']
    success_url = reverse_lazy('index')
    success_message = 'Thank you, %(name)s! We will email you when we have more information about %(cruise)s!'
