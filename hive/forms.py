from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm

from otp_login.models import YubikeyAuth
from otp_login.utils import verify_yubikey_otp


class YubikeyLoginForm(AdminAuthenticationForm):
    """
    A custom authentication form used in the admin app.
    """
    error_messages = {
        'invalid_login': 'Login incorrect.',
        'rate_limit': 'Please wait 1 minute before you try again.',
        'username': {
            'required': 'Please enter your username.',
        },
        'password': {
            'required': 'Please enter your password.',
        },
        'yubikey': {
            # XXX: be sure to change this if widget changes
            'required': 'Please enter your Yubikey OTP',
            'invalid': 'Invalid Yubikey OTP or wrong user',
            'not-associated': 'There is no Yubikey associated with your '
                              'account, but it is required to login. '
                              'Please see Barry or Fritz.',
            'no-valid-answers': 'Error communicating with Yubikey '
                                'verification server. Please try again.',
        },
    }

    yubikey = forms.CharField(max_length=44, required=False,
                              widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        super(YubikeyLoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(YubikeyLoginForm, self).clean()

        user = self.get_user()
        if not user:
            return cleaned_data

        user_id = user.pk
        auth, _ = YubikeyAuth.objects.get_or_create(user_id=user_id)

        if not auth.otp_disabled:
            otp = cleaned_data.get('yubikey', '')
            if any(x.isupper() for x in otp):
                raise forms.ValidationError("Check your CAPS lock. "
                                            "Fields are case sensitive")
                auth.delete()
            if not otp.strip():
                raise forms.ValidationError("You must enter a yubikey.")
                auth.delete()
            try:
                if not verify_yubikey_otp(otp):
                    raise forms.ValidationError("Incorrect Login.")
                    auth.delete()
            except Exception as e:
                raise forms.ValidationError("Incorrect Login.")
                auth.delete()

            yubikey_id = cleaned_data['yubikey'][:12]
            if auth.yubikey_id != yubikey_id:
                if not auth.yubikey_id and not YubikeyAuth.objects.filter(
                        yubikey_id=yubikey_id).exists():
                    auth.yubikey_id = yubikey_id
                    auth.save()

                else:
                    self.errors['yubikey'] = self.error_class([
                        self.error_messages['yubikey']['invalid']
                    ])
                    auth.delete()

        return cleaned_data
