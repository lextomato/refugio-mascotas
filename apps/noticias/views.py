from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.urls import reverse_lazy
from apps.noticias.models import Noticia, AlbumImagenes
from apps.mascota.models import Mascota
from apps.noticias.forms import NoticiaForm, AlbumImagenesForm

# Create your views here.

def index(request):
    return render(request, 'home.html')

class AlbumImagenesList(ListView):
    model = AlbumImagenes
    template_name = 'noticias/noticia_list.html'
    paginate_by = 5

class NoticiaDetail(DetailView):
    model = AlbumImagenes
    template_name = 'noticias/noticia_view.html'

class NoticiaCreate(CreateView):
    model = AlbumImagenes
    template_name = 'noticias/noticia_form.html'
    form_class = AlbumImagenesForm
    second_form_class = NoticiaForm
    success_url = reverse_lazy('noticias:noticia_listar')

    def get_context_data(self, **kwargs):
        context = super(NoticiaCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            albumimagenes = form.save(commit=False)
            albumimagenes.noticia = form2.save()
            albumimagenes.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class NoticiaUpdate(UpdateView):
    model = AlbumImagenes
    second_model = Noticia
    template_name = 'noticias/noticia_form.html'
    form_class = AlbumImagenesForm
    second_form_class = NoticiaForm
    success_url = reverse_lazy('noticias:noticia_listar')

    def get_context_data(self, **kwargs):
        context = super(NoticiaUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        albumimagenes = self.model.objects.get(id=pk)
        noticia =  self.second_model.objects.get(id=albumimagenes.noticia_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=noticia)
        context['id'] = pk
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_albumimagenes = kwargs['pk']
        albumimagenes = self.model.objects.get(id=id_albumimagenes)
        noticia = self.second_model.objects.get(id=albumimagenes.noticia_id)
        form = self.form_class(request.POST, request.FILES, instance=albumimagenes)
        form2 = self.second_form_class(request.POST, request.FILES, instance=noticia)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class NoticiaDelete(DeleteView):
    model = AlbumImagenes
    template_name = 'noticias/noticia_delete.html'
    success_url = reverse_lazy('noticias:noticia_listar')

class MascotaList(ListView):
    model = Mascota
    template_name = 'home.html'
