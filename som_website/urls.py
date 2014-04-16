from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^$',
     TemplateView.as_view(template_name='home.html')),
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact-page'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about-page'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)
