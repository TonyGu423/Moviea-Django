from django.conf.urls import patterns, include, url
from django.contrib import admin
from moviea_django.views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moviea_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
)
