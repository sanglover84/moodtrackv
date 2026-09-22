from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

class BlogListView(ListView):
  model = Post
  template_name = "home.html"
  ordering = ['-date']

class BlogDetailView(DetailView):
  model = Post
  template_name = "post_detail.html"

class BlogCreateView(CreateView):
  model = Post
  template_name = "post_new.html"
  fields = ["author", "mood", "feelings", "energy", "body"]

class BlogUpdateView(UpdateView):
  model = Post
  template_name = "post_edit.html"
  fields = ["mood", "feelings", "energy", "body"]

class BlogDeleteView(DeleteView):
  model = Post
  template_name = "post_delete.html"
  success_url = reverse_lazy("home")

#def post_list(request):
#    posts = Post.objects.all()
#    return render(request, 'home.html',{'posts':posts})

#def post_detail(request,pk):
#   post = get_object_or_404(Post, pk=pk)
 #  return render(request, "post_detail.html", {"post":post})



def chart_view(request):
  # Get data sorted by date
  entries = Post.objects.order_by("-date")

  # Extract dates and moods into separate lists
  dates = [entry.date.strftime("%Y-%m-%d") for entry in entries]
  moods = [entry.mood for entry in entries]  # Assuming a numeric score

  context = {
      "dates": dates,
      "moods": moods,
  }
  return render(request, "chart.html", context)

