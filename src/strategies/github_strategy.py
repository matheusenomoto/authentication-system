from .base_strategy import AuthenticationStrategy

class GitHubStrategy(AuthenticationStrategy):
    '''
    Concrete Strategy for 'Sign in with GitHub'.
    This would also use an OAuth2 flow in a real application.
    '''
    def authenticate(self, **credentials) -> tuple[bool, str]:
        token = credentials.get('token')
        username = credentials.get('username')

        if not token or not username:
            return False, 'GitHub OAuth token and username are required.'

        # Mock validation
        if token == 'valid_github_token':
            return True, f'Successfully authenticated user {username} with GitHub.'
        else:
            return False, 'Invalid GitHub OAuth token.'