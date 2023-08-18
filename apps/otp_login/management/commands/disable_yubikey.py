from django.contrib.auth.models import User
from django.core.management.base import CommandError, LabelCommand

from otp_login.models import YubikeyAuth


class Command(LabelCommand):
    label = 'username'
    help = 'Disable Yubikey authentication for a user'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='+')

    def handle_label(self, username, **options):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError('User "{}" does not exist!'.format(username))
        else:
            auth, _ = YubikeyAuth.objects.get_or_create(user_id=user.pk)
            auth.otp_disabled = True
            auth.save()

            self.stdout.write(
                'Disabled Yubikey authentication for {}'.format(username))
