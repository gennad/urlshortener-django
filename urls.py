from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'urlshortener_prj.urlshortener.views.index', name='home'),
    url(r'^generate/$', 'urlshortener_prj.urlshortener.views.generate'),
    url(r'^.+/$', 'urlshortener_prj.urlshortener.views.redirect'),

    # url(r'^pomadoro_prj/', include('pomadoro_prj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
