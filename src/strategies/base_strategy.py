from abc import ABC, abstractmethod

class AuthenticationStrategy (ABC):
    '''
    The Strategy interface declares operations common to all supported versions
    of some algorithm. The context uses this interface to call the algorithm
    defined by a Concrete Strategy.
    '''
    @abstractmethod
    def authenticate(self, **credentials) -> tuple[bool, str]:
        '''
        Authenticates a user with the given credentials.

        :param credentials: A dictionary of credentials (e.g., username, password, token).
        :return: A tuple containing a boolean (success/failure) and a message.
        '''
        pass
    