from django.conf.urls import patterns, include, url

from django.contrib import admin
from orders.views import DataImportView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', DataImportView.as_view())
)
