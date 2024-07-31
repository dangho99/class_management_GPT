from abc import ABCMeta

class AbstractService:
    __metaclass__ = ABCMeta

    def __init__(self, trans_session):
        self.trans_session = trans_session
