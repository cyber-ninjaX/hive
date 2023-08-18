from django.contrib.auth.models import User, Group
from django.shortcuts import render, get_object_or_404

from passwords.models import Password

from .utils import is_superuser
from .models import AuditEvent


@is_superuser
def audit(request):
    """List a whole bunch of information for superusers to audit."""
    superusers = User.objects.filter(is_superuser=True).order_by('username')
    normoids = _get_normoids().order_by('username')
    passwords = Password.objects.all().order_by('name')
    groups = Group.objects.all().order_by('name')

    context = {
        'superusers': superusers,
        'normoids': normoids,
        'passwords': passwords,
        'groups': groups,
    }
    return render(request, 'audit/audit.html', context)


@is_superuser
def audit_user(request, user_id):
    """Audit a specific user."""
    audited_user = get_object_or_404(User, pk=user_id)
    passwords = {password: password.is_owned_by(audited_user) for password in Password.objects.all() if password.is_owned_by(audited_user)}
    events = AuditEvent.objects.filter(who=audited_user).order_by('-created')
    event_passwords = AuditEvent.objects.filter(who=audited_user, what__regex=r'.*/admin/passwords/password/\d+/change/').order_by('-created')

    context = {
        'audited_user': audited_user,
        'passwords': passwords,
        'audit_events': events,
        'event_passwords': event_passwords,
        'audit_events_count': events.count(),
    }
    return render(request, 'audit/user.html', context)


@is_superuser
def audit_password(request, password_id):
    """Audit a specific password."""
    superusers = User.objects.filter(is_superuser=True).order_by('username')
    audited_password = get_object_or_404(Password, pk=password_id)
    normoids = {user: audited_password.is_owned_by(user) for user in
                _get_normoids() if audited_password.is_owned_by(user)}

    context = {
        'superusers': superusers,
        'audited_password': audited_password,
        'normoids': normoids,
    }
    return render(request, 'audit/password.html', context)


@is_superuser
def audit_group(request, group_id):
    """Audit a specific group."""
    audited_group = get_object_or_404(Group, pk=group_id)

    context = {
        'audited_group': audited_group,
    }
    return render(request, 'audit/group.html', context)


@is_superuser
def audit_event(request, event_id):
    event = get_object_or_404(AuditEvent, pk=event_id)

    context = {
        'event': event,
    }
    return render(request, 'audit/event.html', context)


def _get_normoids():
    return User.objects.filter(is_active=True, is_staff=True,
                               is_superuser=False)
