from django.conf.urls.defaults import patterns, include, url
from mysite.wrflgroove.models import Playlist, DJ
from mysite.wrflgroove import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', 'django.views.generic.simple.direct_to_template', { 'template': '/home/thingummajig/mysite/static/index.html' }),
        url(r'^wrflgroove/$', 'django.views.generic.list_detail.object_list', { 'queryset': DJ.objects.all().order_by('name')}),  
        url(r'^wrflgroove/update_playlist/$', views.update_playlist),
        url(r'^wrflgroove/dj/(?P<dj_name>[a-zA-Z]+)$', views.track_list),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

# Uncomment these two lines to enable your static files on PythonAnywhere
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

