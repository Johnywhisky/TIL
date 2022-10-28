from typing import Union


class AboutMe(object):

    def __init__(self, name: str = "", job: str = "Backend Developer", salary: Union[int, float] = 0) -> None:
        self.name = name
        self.job = job
        self.salary = salary

    @property
    def name(self):
        '''Get attribute value of name'''
        if not hasattr(self, "_name"):
            raise ValueError("Instance has no name. it might be deleted")
        return self._name

    @name.setter
    def name(self, name):
        '''Set attribute value of name'''
        if type(name) is not str:
            raise TypeError("name must be string")
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    def __repr__(cls):
        return cls._name


class SingletonClass(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_isinit"):
            cls._isinit = super().__new__(cls)
        return cls._isinit

    def __init__(self, name, job):
        self.job = job
        self._name = name


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):
            print("__init__ is called\n")
            self.data = data
            cls._init = True


me = AboutMe(name="John")
print(me)