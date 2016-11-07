from django.conf.urls import url

from .views import IndexView
from .views import SuModelCreate, SuModelDelete, SuObjects, SuObjectUpdate, SuObjectCreate, SuObjectDelete

urlpatterns = [

    # Index
    url(r'^$', IndexView.as_view(), name='su_index'),

    # Model
    url(r'^model/create/$', SuModelCreate.as_view(), name='su_model_create'),
    url(r'^model/(?P<pk>\w+)/delete$', SuModelDelete.as_view(), name='su_model_delete'),

    # Object
    url(r'^object/(?P<model>\w+)/$', SuObjects.as_view(), name='su_objects'),
    url(r'^object/(?P<model>\w+)/create/$', SuObjectCreate.as_view(), name='su_object_create'),
    url(r'^object/(?P<model>\w+)/(?P<pk>\d+)/$', SuObjectUpdate.as_view(), name='su_object_update'),
    url(r'^object/(?P<model>\w+)/(?P<pk>\d+)/delete/$', SuObjectDelete.as_view(), name='su_object_delete'),

]
