from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from .models import Opinion, Cruise
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

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

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
#from .forms import InfoRequestForm

#def info_request(request):
#    if request.method == 'POST':
#        form = InfoRequestForm(request.POST)
#        if form.is_valid():
#            form.save()
#            send_mail(
#                'Solicitud de Información Recibida',
#                'Hemos recibido su solicitud de información.',
#                settings.EMAIL_HOST_USER,
#                [form.cleaned_data['email']],
#                fail_silently=False,
#            )
#            return redirect('info_request_success')
#    else:
#        form = InfoRequestForm()
#    return render(request, 'info_request.html', {'form': form})

# views.py
#def info_request_success(request):
#    return render(request, 'info_request_success.html')


        

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
    success_url = reverse_lazy('info_request_success')
    success_message = 'Thank you, %(name)s! We will email you when we have more information about %(cruise)s!'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)