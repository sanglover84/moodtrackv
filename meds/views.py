from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MedsPost
from django.urls import reverse_lazy 
# new views
class MedsListView(ListView):
    model = MedsPost
    template_name = "meds.html"

class MedsDetailView(DetailView):
    model = MedsPost
    template_name = "medspost_detail.html"
    
# Create your views here.
#def medspost_list(request):
 #   medsposts = MedsPost.objects.all()
 #   return render(request, "meds.html",{'medsposts':medsposts})

def meds_page(request):
    return render(request, "meds.html")

#def medspost_detail(request, pk):
#    medspost = get_object_or_404(MedsPost, pk=pk)
 #   return render(request, "medspost_detail.html",{"medspost":medspost})

class MedsCreateView(CreateView):
    model = MedsPost
    template_name = "meds_new.html"
    fields = {"author", "medname", "generic", "totaldose", "dose1", "dose2", "dose3", "frequency", "type", "whatfor", "sideeffects"}

class MedsUpdateView(UpdateView):
    model = MedsPost
    template_name = "meds_edit.html"
    fields =  {"author", "medname", "generic", "totaldose", "dose1", "dose2", "dose3", "frequency", "type", "whatfor", "sideeffects"}

class MedsDeleteView(DeleteView):
    model = MedsPost
    template_name = "meds_delete.html"
    success_url = reverse_lazy("home")

