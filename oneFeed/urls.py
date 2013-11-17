from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import hello, add_competer, added_competer, display_results

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oneFeed.views.home', name='home'),
    # url(r'^oneFeed/', include('oneFeed.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^add/$', add_competer),
    url(r'^display/$', display_results),
#    url(r'^added_competer/$', added_competer),
) + staticfiles_urlpatterns() 
