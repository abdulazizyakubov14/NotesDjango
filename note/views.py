from django.db import models
from django.db.models import query
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from .models import Notes
# Create your views here.

class HomeView(ListView):
    model = Notes
    template_name = 'index.html'
    ordering = ['-id']

class CreateNote(CreateView):
    model = Notes
    fields = '__all__'
    template_name = 'create.html'
    success_url = '/'

class UpdateNote(UpdateView):
    model = Notes
    fields = '__all__'
    template_name = 'create.html'
    success_url = '/'


class DeletNote(DeleteView):
    model = Notes
    success_url = '/'
    template_name = 'delet.html'

def search(request):
    s = request.GET.get('search',None)
    note = Notes.objects.filter(title__icontains=s)
    context = {
        'note':note,
        
    }

    return render(request,'search.html',context)