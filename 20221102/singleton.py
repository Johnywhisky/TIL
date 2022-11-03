from collections import defaultdict


class SingletonMeta(type):
    _instances = defaultdict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        print(f"input kwargs: {kwargs}")
        return cls._instances[cls]


class SingletonWithMetaClass(metaclass=SingletonMeta):
    def __init__(self, **kwargs):
        self._name: str = kwargs["name"]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        setattr(self, "_name", name)

    @name.deleter
    def name(self):
        del self._name

    def __repr__(self) -> str:
        return f"this class is {self.name}'s class"


class SingletonWithNewMethod(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print("__new__ is called", end="\n")
            cls._instance = super().__new__(cls)
            print(f"input kwargs: {kwargs}")
        return cls._instance

    def __init__(self, **kwargs):
        cls = type(self)
        if not hasattr(cls, "_init"):
            print("__init__ is called", end="\n")
            self._name = kwargs["name"]
            print(f"input kwargs: {kwargs}")
            cls._init = True

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        setattr(self, "_name", name)

    @name.deleter
    def name(self) -> None:
        del self._name

    def __repr__(self) -> str:
        return f"this class is {self.name}'s class"


from threading import Lock, Thread


class SingletonMultiThread(type):
    _instances = defaultdict()
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonMultiThread(metaclass=SingletonMultiThread):
    _name = None

    def __init__(self, **kwargs) -> None:
        self._name: str | None = kwargs.get("name")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        setattr(self, "_name", name)

    @name.deleter
    def name(self) -> None:
        del self._name

    def __repr__(self) -> str:
        return f"this class is {self.name}'s class"


def test_singleton(name: str) -> None:
    smt = SingletonMultiThread(name=name)
    print(smt.name)


if __name__ == "__main__":

    p1 = SingletonWithMetaClass(name="John")
    p2 = SingletonWithMetaClass(name="Ming")

    print(p1.name, p2.name)
    print(id(p1), id(p2))

    p3 = SingletonWithNewMethod(name="John")
    p4 = SingletonWithNewMethod(name="Ming")

    print(p3.name, p4.name)
    print(id(p3), id(p4))

    p5 = Thread(target=test_singleton, args=["John"])
    p6 = Thread(target=test_singleton, args=["Ming"])
    p5.start()
    p6.start()
