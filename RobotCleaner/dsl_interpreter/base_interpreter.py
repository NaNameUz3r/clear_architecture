

from abc import ABCMeta, abstractmethod
class BaseInterpreter(metaclass=ABCMeta):

    @abstractmethod
    def interpret(self, command: str) -> str:
        """Interpret the command"""
        pass
    pass