class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def algorithm_interface(self):
        pass
