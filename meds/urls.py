from django.urls import path
from .views import MedsListView, MedsDetailView, MedsCreateView, MedsUpdateView, MedsDeleteView

urlpatterns = [
    path("meds/new", MedsCreateView.as_view(), name="meds_new"),
    path("meds/", MedsListView.as_view(), name="meds_page"),
    path("medspost/<int:pk>/", MedsDetailView.as_view(), name="medspost_detail"),
    path("medspost/<int:pk>/edit/",MedsUpdateView.as_view(),name="meds_edit"),
    path("medspost/<int:pk>/delete/",MedsDeleteView.as_view(),name="meds_delete"),
    path("meds/",MedsListView.as_view(), name="meds_page"),

]