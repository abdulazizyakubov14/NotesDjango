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
    paginate_by = 4

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
    q = request.GET.get('search',None)
    note = Notes.objects.filter(title__icontains=q)
    res = len(note)
    context = {
        'res':res,
        'note':note,
        
    }

    return render(request,'serach.html',context)