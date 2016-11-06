from django.conf.urls import url

from .views import IndexView
from .views import SuModelCreate, SuModelDelete

urlpatterns = [

    # Index page
    url(r'^$', IndexView.as_view(), name='su_index'),

    # SuModel generic views
    url(r'^create/$', SuModelCreate.as_view(), name='su_model_create'),
    url(r'^delete/(?P<pk>\w+)/$', SuModelDelete.as_view(), name='su_model_delete'),

]
