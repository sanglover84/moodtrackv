# your_app/urls.py
from django.urls import path
from . import views
from .views import SymptomsList, SymptomsDetailView, SymptomsCreateView, SymptomsUpdateView, SymptomsDeleteView

urlpatterns = [
    # Map the root or a specific path (e.g., 'products/') to your view
    path('symptoms/new/', views.SymptomsCreateView.as_view(), name='symptoms_new'), 
    path("symptoms/<int:pk>/edit", SymptomsUpdateView.as_view(), name="symptoms_edit"),
    path("symptoms/<int:pk>/delete/", SymptomsDeleteView.as_view(), name="symptoms_delete"),
    path("symptoms/<int:pk>/", SymptomsDetailView.as_view(), name="symptoms_detail"),
    path('symptoms/', SymptomsList.as_view(), name='symptoms'),
]