from django.shortcuts import render, HttpResponse
from relecloud import models
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# views.py
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import InfoRequestForm

def info_request(request):
    if request.method == 'POST':
        form = InfoRequestForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Solicitud de Información Recibida',
                'Hemos recibido su solicitud de información.',
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('info_request_success')
    else:
        form = InfoRequestForm()
    return render(request, 'info_request.html', {'form': form})


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

