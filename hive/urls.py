from django.conf.urls import include, url
from django.shortcuts import redirect
from hive.forms import YubikeyLoginForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
admin.site.login_form = YubikeyLoginForm

urlpatterns = [
    url(r'^$', lambda r: redirect('admin/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^audit/', include('audit.urls')),
]
