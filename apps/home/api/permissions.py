def has_mac_permissions(token=None, user_token=None):
    if not token or not user_token:
        return False

    return user_token == token
