from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'homepage.views.home', name='home'),
    url(r'^about/$','homepage.views.about', name='about'),
    url(r'^contact/$','homepage.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
]
