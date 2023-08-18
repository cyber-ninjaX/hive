from .models import AuditEvent
from passwords.models import Password


class AuditEventMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            return
        if not any([
            request.path_info.startswith('/audit'),
            request.path_info.startswith('/static'),
            request.path_info.startswith('/media'),
            request.path_info == '/admin/jsi18n/',
        ]):
            what = u"{} {}".format(request.method, request.path_info)
            post = {k: v for k, v in request.POST.items() if k != 'password'}
            payload = repr(request) + "\n\nGET: " + repr(dict(request.GET)) + \
                "\n\nPOST:" + repr(post)
            AuditEvent.objects.create(who=request.user, what=what,
                                      payload=payload)
