# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota, Categoria

# Create your views here.

def listado(request):
    lista = serializers.serialize('json', Mascota.objects.all(), fields=['nombre', 'edad_aproximada', 'categoria'])
    return HttpResponse(lista, content_type='application/json')

def index(request):
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    else:
        form = MascotaForm()
    
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascota':mascota}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'
    paginate_by = 5

class MascotaListGeneral(ListView):
    model = Mascota
    second_model = Categoria
    template_name = 'mascota/mascota_general.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(MascotaListGeneral, self).get_context_data(**kwargs)
        context['obj1'] = self.model.objects.all()
        context['obj2'] = self.second_model.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        obj1 = self.model.objects.all()
        obj2 = Categoria.objects.all()
        if request.POST.get('especie') != 'Especie...' and request.POST.get('raza') == 'Raza...':
            especie = request.POST.get('especie')
            obj1 = obj1.filter(categoria__especie=especie)
            return render(request, "mascota/mascota_general.html", {'obj1': obj1, 'obj2': obj2, 'especie':especie})
        if request.POST.get('raza') != 'Raza...' and request.POST.get('especie') == 'Especie...':
            raza = request.POST.get('raza')
            obj1 = obj1.filter(categoria__raza=raza)
            return render(request, "mascota/mascota_general.html", {'obj1': obj1, 'obj2': obj2, 'raza':raza})
        return render(request, "mascota/mascota_general.html", {'obj1': obj1, 'obj2': obj2, 'raza':raza})

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaDelete(DeleteView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaDetail(DetailView):
    model = Mascota
    template_name = 'mascota/mascota_view.html'
