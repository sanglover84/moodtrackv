from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sleep

class SleepListView(ListView):
    model = Sleep
    template_name = "sleep.html"

class SleepDetailView(DetailView):
    model = Sleep
    template_name = "sleep_detail.html"

class SleepCreateView(CreateView):
    model = Sleep
    template_name = "sleep_new.html"
    fields = ["author", "hourssleep", "notes"]

class SleepUpdateView(UpdateView):
    model = Sleep
    template_name = "sleep_edit.html"
    fields = ["author", "hourssleep", "notes"]

class SleepDeleteView(DeleteView):
    model = Sleep
    template_name = "sleep_delete.html"
    success_url = reverse_lazy("sleep")

def sleep_chart_view(request):
    entries = Sleep.objects.order_by("-datetime")
    
    dates = [entry.datetime.strftime("%Y-%m-%d") for entry in entries]
    hourssleep = [entry.hourssleep for entry in entries] 

    context = {
        "dates": dates,
        "hourssleep": hourssleep, # Must be spelled exactly like this
    }
    return render(request, "sleep_chart.html", context)

# Create your views here.
#def sleep_list(request):
#    sleeps = Sleep.objects.all()
#    return render(request, "sleep.html", {'sleeps':sleeps})
#
#def sleep_detail(request, pk):
#    sleep = get_object_or_404(Sleep, pk=pk)
#    return render(request, "sleep_detail.html", {"sleep": sleep})