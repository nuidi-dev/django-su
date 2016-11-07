from django.shortcuts import render
from django.urls import reverse

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import UserPassesTestMixin

from django.views.generic.edit import FormMixin
from django.views.generic.edit import ProcessFormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from .models import SuModel

from .forms import SuModelForm

class SuPermissionMixin(UserPassesTestMixin):
    """ Mixin for checking user permissions for suadmin access """

    def test_func(self):
        try:
            return self.request.user.is_superuser
        except AttributeError:
            return False

class SuMixin(object):

    """ Mixing for adding model name into context and setting queryset """

    def get_queryset(self):
        return ContentType.objects.get(model=self.kwargs['model']).get_all_objects_for_this_type()

    def get_context_data(self, **kwargs):
        context = super(SuMixin, self).get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model']
        return context

class IndexView(SuPermissionMixin, ListView, FormMixin):
    model = SuModel
    fields = '__all__'
    form_class = SuModelForm
    template_name = 'su/index.html'

class SuModelCreate(SuPermissionMixin, CreateView, ProcessFormView):
    model = SuModel
    fields = '__all__'

    def get_success_url(self):
        return reverse('su_index')

class SuModelDelete(SuPermissionMixin, DeleteView):
    model = SuModel

    def get_success_url(self):
        return reverse('su_index')

class SuObjects(SuPermissionMixin, SuMixin, ListView):
    template_name = 'su/su_objects_list.html'

class SuObjectCreate(SuPermissionMixin, SuMixin, CreateView, ProcessFormView):
    template_name = 'su/su_object_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('su_objects', args=(self.kwargs['model'],))

class SuObjectUpdate(SuPermissionMixin, SuMixin, UpdateView):
    template_name = 'su/su_object_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('su_objects', args=(self.kwargs['model'],))

class SuObjectDelete(SuPermissionMixin, SuMixin, DeleteView):
    template_name = 'su/su_object_confirm_delete.html'
    model = SuModel

    def get_success_url(self):
        return reverse('su_objects', args=(self.kwargs['model'],))
