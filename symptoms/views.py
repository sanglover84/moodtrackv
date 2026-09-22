from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Symptom
from django.urls import reverse_lazy

# Create your views here.
#def symptom_table_view(request):
#    symptoms = Symptom.objects.all()
#    return render(request, 'symptoms_table.html', {'symptoms': symptoms})
class SymptomsList(ListView):
    model = Symptom
    template_name = "symptoms_table.html"

#def symptoms_detail(request, pk):
#    symptom = get_object_or_404(Symptom, pk=pk)
#    return render(request, "symptoms_detail.html",{"symptom":symptom})

#class SymptomsListView(ListView):
#    model = Symptom
#    template_name = "symptoms_table.html"

class SymptomsDetailView(DetailView):
    model = Symptom
    template_name = "symptoms_detail.html"

class SymptomsCreateView(CreateView):
    model = Symptom
    template_name = "symptoms_new.html"
    fields = ["author", "notes", "Anxiety", "Depression", "Mania", "Paranoia", "IdeasOfReference", "Hallucinations", "Fatigue", "Insomnia", "Restlessness", "Agitation", "WristPain", "ShoulderPain"]

class SymptomsUpdateView(UpdateView):
    model = Symptom
    template_name = "symptoms_edit.html"
    fields = ["author", "notes", "Anxiety", "Depression", "Mania", "Paranoia", "IdeasOfReference", "Hallucinations", "Fatigue", "Insomnia", "Restlessness", "Agitation", "WristPain", "ShoulderPain"]

class SymptomsDeleteView(DeleteView):
    model = Symptom
    template_name = "symptoms_delete.html"
    success_url = reverse_lazy("home")