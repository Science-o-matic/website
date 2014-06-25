from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from contact_form.views import ContactFormView
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$',
                           TemplateView.as_view(template_name='home.html')),
                       url(r'^contact/$',
                           csrf_exempt(ContactFormView.as_view()),
                           name='contact_form'),
                       url(r'^contact/sent/$',
                           TemplateView.as_view(
                               template_name='contact_form/contact_form_sent.html'
                               ),
                           name='contact_form_sent'),
#                       url(r'^about/$',
#                           TemplateView.as_view(template_name='about.html'),
#                           name='about-page'),
                       (r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'^admin/', include(admin.site.urls)),
)
