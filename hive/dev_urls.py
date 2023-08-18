from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from hive.urls import urlpatterns


# handle media urls through django
urlpatterns +=  urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


## redirect for favicon
#urlpatterns += patterns('',
#    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {
#        'url': '/static/images/favicon.ico',
#    }),
#)
