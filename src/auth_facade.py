from .strategies.local_strategy import LocalStrategy
from .strategies.google_strategy import GoogleStrategy
from .strategies.github_strategy import GitHubStrategy

# Singleton Decorator
def singleton(class_):
    '''
    A decorator to implement the Singleton pattern.
    '''
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@singleton
class AuthenticationFacade:
    '''
    The Facade class provides a simple interface to the complex logic of one or
    several subsystems. The Facade delegates client requests to the appropriate
    objects within the subsystem.

    This class is also a Singleton, ensuring only one instance exists.
    '''
    def __init__(self):
        self._strategies = {
            'local': LocalStrategy(),
            'google': GoogleStrategy(),
            'github': GitHubStrategy(),
        }
        print('AuthenticationFacade instance created.')

    def authenticate(self, strategy_name: str, **credentials) -> tuple[bool, str]:
        '''
        The main method of the facade. It selects the appropriate strategy
        and delegates the authentication task to it.
        
        :param strategy_name: The name of the strategy to use ('local', 'google', 'github').
        :param credentials: The credentials required by the chosen strategy.
        :return: A tuple containing a boolean (success/failure) and a message.
        '''
        strategy = self._strategies.get(strategy_name.lower())
        if not strategy:
            return False, f'Authentication strategy {strategy_name} not supported.'

        print(f'\n--- Attempting authentication with {strategy_name} strategy ---')
        success, message = strategy.authenticate(**credentials)
        print(message)
        return success, message
