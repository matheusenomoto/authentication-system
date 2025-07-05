from .base_strategy import AuthenticationStrategy
from ..mock_user_db import MockUserDB

class LocalStrategy(AuthenticationStrategy):
    '''
    Concrete Strategy for authenticating users with a username and password.
    '''
    def __init__(self):
        self._db = MockUserDB()
    
    def authenticate(self, **credentials) -> tuple[bool, str]:
        username = credentials.get('username')
        password = credentials.get('password')

        if not username or not password:
            return False, 'Username and password are required'
        
        user = self._db.get_user(username)
        if user and user['password'] == password:
            return True, f'Successfully authenticated user {username} locally'
        else:
            return False, 'Invalid username or password'
