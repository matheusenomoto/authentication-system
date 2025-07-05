from src.auth_facade import AuthenticationFacade

def main():
    '''
    Client code that uses the AuthenticationFacade to perform authentication.
    The client interacts with a simple interface, unaware of the complexity behind it.
    '''
    # Get the Singleton instance of the facade
    auth_manager_1 = AuthenticationFacade()
    auth_manager_2 = AuthenticationFacade()

    # Demonstrate that it's a Singleton
    print(f'\nIs auth_manager_1 the same instance as auth_manager_2? {auth_manager_1 is auth_manager_2}')

    # --- Use Case 1: Local Authentication ---
    # Successful login
    auth_manager_1.authenticate('local', username='admin', password='topPwdrsrs')

    # Failed login
    auth_manager_1.authenticate('local', username='admin', password='wrongpassword')
    
    # --- Use Case 2: Google Authentication ---
    # Successful login
    auth_manager_1.authenticate('google', email='user@gmail.com', token='valid_google_token')

    # Failed login
    auth_manager_1.authenticate('google', email='user@gmail.com', token='invalid_token')

    # --- Use Case 3: GitHub Authentication ---
    # Successful login
    auth_manager_1.authenticate('github', username='dev-user', token='valid_github_token')

    # --- Use Case 4: Unsupported Strategy ---
    auth_manager_1.authenticate('facebook', user_id='12345')


if __name__ == '__main__':
    main()