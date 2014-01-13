from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from content.views import hello

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', hello),
    #url(r'^$', BaseView.as_view(template_name='base.html')),
    url(r'^images/', include('photologue.urls')),



    # Examples:
    # url(r'^$', 'amanodzjaku.views.home', name='home'),
    # url(r'^amanodzjaku/', include('amanodzjaku.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))