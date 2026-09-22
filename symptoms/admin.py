from django.contrib import admin
from .models import Symptom
# Register your models here.

class SymptomAdmin(admin.ModelAdmin):
    list_display = (
        "datetime",
        "notes", 
        "Anxiety",
        "Depression",
        "Mania",
        "Paranoia",
        "IdeasOfReference",
        "Hallucinations",
        "Fatigue",
        "Insomnia",
        "Restlessness",
        "Agitation",
        "WristPain",
        "ShoulderPain",
    )

admin.site.register(Symptom, SymptomAdmin)