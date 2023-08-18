from django.conf.urls import url
from .views import audit, audit_group, audit_user, audit_password, audit_event


urlpatterns = [
    url(r'^$', audit, name='audit'),
    url(r'^user/(?P<user_id>\d+)/$', audit_user, name='audit-user'),
    url(r'^password/(?P<password_id>\d+)/$', audit_password, name='audit-password'),
    url(r'^group/(?P<group_id>\d+)/$', audit_group, name='audit-group'),
    url(r'^event/(?P<event_id>\d+)/$', audit_event, name='audit-event'),
]
