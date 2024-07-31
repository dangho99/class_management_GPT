from abc import ABCMeta, abstractmethod

class LLMParams:
    __metaclass__ = ABCMeta
    
    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            if type(v) == dict:
                v = LLMParams(**v)
            self[k] = v
            
    def keys(self):
        return self.__dict__.keys()

    def items(self):
        return self.__dict__.items()

    def values(self):
        return self.__dict__.values()

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __contains__(self, key):
        return key in self.__dict__

    def __repr__(self):
        return self.__dict__.__repr__()