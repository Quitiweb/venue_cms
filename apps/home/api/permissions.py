from rest_framework.authtoken.models import Token

from users.models import MacUser


def has_mac_permissions(mac=None, token=None):
    if not token:
        return False
    if not mac:
        return False

    try:
        mac_user = MacUser.objects.get(username=mac.replace(":", ""))
    except MacUser.DoesNotExist:
        return False

    try:
        user_token = Token.objects.get(user=mac_user)
    except Token.DoesNotExist:
        return False

    return user_token.key == token
