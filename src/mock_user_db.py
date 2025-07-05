
class MockUserDB:
    '''
    A mock database to store user credentials for local authentication.
    In a real-world application, this would be a connection to a real database
    (e.g., PostgreSQL, DynamoDB).
    '''
    _users = {
        'admin': {
            'password': 'topPwdrsrs',
            'roles': ['admin', 'editor']
        },
        'testuser': {
            'password': 'pwd',
            'roles': ['viewer']
        }
    }

    def get_user(self, username: str) -> dict | None:
        return self._users.get(username)