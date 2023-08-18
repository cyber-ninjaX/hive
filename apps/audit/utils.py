from functools import wraps

from django.http import Http404


def is_superuser(view):
    """Django view decorator that tests to make sure the user is logged in
    and is a superuser."""
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        user = getattr(request, 'user', None)
        if user and user.is_superuser:
            return view(request, *args, **kwargs)
        else:
            raise Http404
    return wrapper
