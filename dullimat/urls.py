from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('devices.views',
    url(r'^devices/$', 'index', name='index'),
	url(r'^devices/(?P<device_id>\d+)/$', 'switch'),
	# url(r'^$', 'dullimat.views.home', name='home'),
    # url(r'^dullimat/', include('dullimat.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
