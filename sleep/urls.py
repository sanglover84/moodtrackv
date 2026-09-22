from django.urls import path
from .views import SleepListView, SleepDetailView, SleepCreateView, SleepUpdateView, SleepDeleteView
from . import views

urlpatterns = [
    path("sleep/new/", SleepCreateView.as_view(), name="sleep_new"),
    path("sleep/<int:pk>/", SleepDetailView.as_view(), name="sleep_detail"),
    path("sleep/<int:pk>/edit/", SleepUpdateView.as_view(), name="sleep_edit"),
    path("sleep/<int:pk>/delete/", SleepDeleteView.as_view(), name="sleep_delete"),
    path("sleep/", SleepListView.as_view(), name="sleep"),
    path('sleepchart/', views.sleep_chart_view, name='sleepchart'),

    #path("sleep/<int:pk>/", sleep_detail, name="sleep_detail"),
    #path("sleep/", sleep_list, name="sleep"),
]