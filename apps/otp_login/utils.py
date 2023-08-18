from django.conf import settings

from yubico_client import Yubico
from yubico_client.yubico_exceptions import StatusCodeError

from otp_login.models import YubikeyAuth


def verify_yubikey_otp(otp):
    yubiver = Yubico(settings.YUBI_CLIENT_ID,
                     api_urls=settings.YUBI_API_URLS, verify_cert=False)
    try:
        return yubiver.verify(otp, timeout=30)
    except StatusCodeError:
        return False


def verify_yubikey_auth(otp, user_id):
    if not verify_yubikey_otp(otp):
        return False

    yubikey_id = otp[:12]
    try:
        YubikeyAuth.objects.get(yubikey_id=yubikey_id, user_id=user_id)
    except YubikeyAuth.DoesNotExist:
        return False
    else:
        return True
