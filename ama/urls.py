from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from qa.models import Qa, Ama
from qa.views import QaListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ama.views.home', name='home'),
    # url(r'^ama/', include('ama.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qa.views.index'),
    url(r'^(?P<amaid>\d+)', QaListView.as_view(template_name="qa.html", context_object_name="all_qas")),
    #url(r'^(?P<amaid>\d+)', ListView.as_view(model=Qa,template_name="qa.html", context_object_name="all_qas")),
)
