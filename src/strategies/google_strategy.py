from .base_strategy import AuthenticationStrategy

class GoogleStrategy(AuthenticationStrategy):
    '''
    Concrete Strategy for 'Sign in with Google'.
    In a real application, this would involve using an OAuth2 library
    to verify the token with Google's servers.
    '''
    def authenticate(self, **credentials) -> [bool, str]:
        token = credentials.get('token')
        email = credentials.get('email')

        if not token or not email:
            return False, 'Google OAuth token and email are required.'

        # Mock validation: In a real scenario, you'd send the token to Google for verification.
        if token == 'valid_google_token':
            return True, f'Successfully authenticated user {email} with Google.'
        else:
            return False, 'Invalid Google OAuth token.'