from django.shortcuts import render
from django.urls import reverse

from django.views.generic.edit import FormMixin
from django.views.generic.edit import ProcessFormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from .models import SuModel

from .forms import SuModelForm

class IndexView(ListView, FormMixin):
    model = SuModel
    form_class = SuModelForm
    fields = '__all__'
    template_name = 'su/index.html'

class SuModelCreate(CreateView, ProcessFormView):
    model = SuModel
    fields = '__all__'

    def get_success_url(self):
        return reverse('su_index')

class SuModelDelete(DeleteView):
    model = SuModel

    def get_success_url(self):
        return reverse('su_index')
