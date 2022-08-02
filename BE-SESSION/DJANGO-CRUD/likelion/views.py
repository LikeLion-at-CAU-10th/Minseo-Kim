from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import LikeLion

# Create your views here.
class LikeLionCreateView(CreateView):
    model = LikeLion
    fields = "__all__"
    #fields = ['name',]
    success_url = "/likelion"

class LikeLionListView(ListView):
    model = LikeLion
    paginate_by = 30
    ordering = ['-name'] # - 붙이면 역순

class LikeLionUpdateView(UpdateView):
    model = LikeLion
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = "/likelion"

class LikeLionDeleteView(DeleteView):
    model = LikeLion
    success_url = "/likelion"

class LikeLionDetailView(DetailView):
    model = LikeLion
    template_name_suffix = '_detail_form'
    success_url = "/likelion"
