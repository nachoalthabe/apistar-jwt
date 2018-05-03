from apistar import http

from .exceptions import AuthenticationFailed


def get_token_from_header(auth: http.Header):
    if auth is None:
        raise AuthenticationFailed('Authorization header is missing.')
    try:
        scheme, token = auth.split()
    except ValueError:
        raise AuthenticationFailed('Could not seperate Authorization scheme and token.')
    if scheme.lower() != 'bearer':
        raise AuthenticationFailed('Authorization scheme not supported, try Bearer')
    return token
