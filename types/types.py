# # type hint
# # varible: type = value
# from typing import (
#     List,
#     Dict,
#     Tuple,
#     Callable,
#     Union, 
#     Optional, 
#     Generic,
#     TypeVar,
#     )
# from typing_extensions import (Final, TypedDict)

# int_var : int = 100
# str_var : str = "Hello World"
# bool_var : bool = True
# list_var : List[str] = ["가", "나", "다"]
# tuple_var : Tuple[int, int, int] = (1, 2, 3)
# dict_var : Dict[str, int] = {"A": hash("A")}

# # # 타입힌트는 타입을 강제하지 않음
# # # ridiculous_dict : Dict[str, int] = {"A": ascii("A"), "B": "ascii('B')"} # 작동 함

# # object, any # 기타 타입에는 이런것도 있다

# # # # 타입힌트의 문제점
# # # def cal_add(x, y):
# # #     return x + y
# # # # => 의도한 함수는 '정수 합을 반환하는 함수' 이지만 힌트가 없기 때문에 +연산이 가능한 모든 변수를 대입해도 된다. => 규모가 커질수록 타인과의 협업 때 문제가 될 수 있음

# # # # ex)
# # # result = cal_add("hi", "JohnyWhisky") # 작동함

# # # # 해결방안
# # # def cal_add(x: int, y: int) -> int:
# # #     return x + y

# # # 하지만 타입 힌트는 변수의 타입을 강제하지 않기 때문에 결국 다른 타입이 들어와도 작동함
# # # --> 해결방안 : type checking

# # def cal_add1(x: int, y: int) -> int:
# #     # sol 1.
# #     if type(x) is int and type(y) is int:
# #         return x + y
# #     else:
# #         raise TypeError

# # def cal_add2(x: int, y: int):
# #     #sol 2.
# #     if isinstance(x, int) and isinstance(y, int):
# #         return x + y
# #     else:
# #         return TypeError

# # # => type check logic 도 함수화시켜준다
# # def type_check(obj, typer):
# #     if isinstance(obj, typer):
# #         pass
# #     else:
# #         raise TypeError(f"{obj} is not {typer} type")

# # def cal_add(x: int, y: int) -> int:
# #     type_check(x, int)
# #     type_check(y, int)
    
# #     return x + y

# # # 이러한 방식은 중요한 함수일수록 권장된다
# # # sudo npm install -g pyright
# # # 생산성을 위해 unittest같은 국소 모듈에 활용하는 걸 추천

# # # Callable types

# # def foo(a: int, b: int) -> int:
# #     return a + b

# # def bar(func: Callable[[int, int], int]) -> str:
# #     return str(func(2, 3))

# # print(bar(foo))

# # # Class types

# # class Hello:
# #     def work(self) -> str:
# #         return "World"

# # hello: Hello = Hello()

# # def foo2(instance: Hello) -> str:
# #     return instance.work()

# # print(foo2(hello))

# # # 클레스 타입을 타입 힌트로 제공할 때 다음과 같이도 가능하다.
# # class World:
# #     def work(self) -> str:
# #         return "Hello"

# # world: "World" = World()
# # def foo2_1(instance: "World") -> str:
# #     return instance.work()

# # # # Union types
# # # x2: int = 3
# # # # x2 = "3" # => pyright에서 error 반환

# # x2: Union[int, str] = 3
# # print(x2)
# # x2 = "4"
# # print(x2)

# # # # Optional types

# # # Union과 비슷하지만, 조금 다른 의미를 가진다
# # # type을 가지거나 None일 경우 -> Union[type, None] 을 Optional[type]으로 대체 가능
# # # ex)

# # x3: Optional[str] = "Hello"
# # # x3 = False # Optional에 bool이 정의되어있지 않아서 Pyright에서 에러 반환

# # def foo3(name: Optional[str]) -> Optional[str]:
# #     if isinstance(name, str):
# #         return name
# #     else:
# #         return None

# # def foo4(name: Union[str, None]) -> Union[str, None]:
# #     if isinstance(name, str):
# #         return name
# #     else:
# #         return None

# # x4: Optional[str] = foo3("johnywhisky")

# # # Optional with Class types

# # class Node(object):
    
# #     def __init__(self, data: int, node: Optional["Node"]=None) -> None:
# #         self.data = data
# #         self.node = node

# #     def __repr__(self):
# #         return str(self.data)

# # node1 = Node(12)
# # node2 = Node(27, node1)
# # node3 = Node(42, node2)
# # print(node2)

# # # Final types

# # # RATE = 300 # 변수를 모두 대문자로 선언할 때 상수를 의미한다(convention)
# # RATE: Final = 300
# # # RATE = 1
# # # Final로 선언 시 같은 type의 값이 재할당되도 pyright에서 에러를 반환한다.
# # # 물론 pyright없이 실행할 경우 잘 실행된다

# # # Type alias
# # val: Union[
# #     int,
# #     bool,
# #     Union[List[str], List[str], Tuple[int, ...]],
# #     Optional[Dict[str, float]]
# #     ] = 1

# # def cal2(
# #     val: Union[
# #         int,
# #         bool,
# #         Union[List[str], List[str], Tuple[int, ...]],
# #         Optional[Dict[str, float]]
# #         ]
# #     ):
# #     return val

# # # 가독성이 너무 안좋다
# # # tpye 자체를 새롭게 정의해주자
# # Special_type = Union[
# #     int,
# #     bool,
# #     Union[List[str], List[str], Tuple[int, ...]],
# #     Optional[Dict[str, float]]
# #     ]
# # def foobal(val: Special_type = True) -> None:
# #     print(val)

# # foobal(["Good"])

# # # json 객체 활용 시

# # # json과 같이 key의 이름과, value의 타입이 확정적이고, 고정적일 때
# # class ThreeDimension(TypedDict):
# #     x: int
# #     y: float
# #     z: str

# # point: ThreeDimension = {
# #     "x": 8,
# #     "y": -10.5,
# #     "z": '13'
# # }
# # print(point)

# # Generic Programming
# # 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술


# # type 생성자
# ARM = TypeVar("ARM")
# HEAD = TypeVar("HEAD")

# class Robot(Generic[ARM, HEAD]):
    
#     def __init__(
#         self,
#         arm: ARM, # -> 2의 crank
#             # Union[int, str], -> 1의 crank
#         head: HEAD) -> None:
#         self.arm = arm
#         self.head = head
    
#     def decode(self):
#         # ... complex decoding code
#         # arm과 같은 type의 변수를 선언할 필요가 있을 때
#         # 1. crank
#         # crank: Optional[Union[int, str]] = None
#         # 이렇게 선언할 경우 arm의 type은 이전 시점에 type이 정해져있으나 crank는 가질 수 있는 타입의 경우가 세개이다.
        
#         # 2. crank
#         crank: Optional[ARM] = None
#         gear: Optional[HEAD] = None
#         pass

# # 1. crank 경우의 instance 생성 방식
# # robot1 = Robot(14532534, 1244125)
# # robot2 = Robot("32425", 1774242)
# # robot3 = Robot(13505710, 329580)

# # instance에 대해 ARM이 어떤 type 역할을 하는지 instance 생성 시 정해준다
# # 2. crank
# robot1 = Robot[int, str](14532534, "1244125")
# robot2 = Robot[str, float]("32425", 17742.42)
# robot3 = Robot[float, int](13505.5103, 329580)

# from typing import Generic, TypeVar


# T = TypeVar("T")
# K = TypeVar("K")

# class Robot(Generic[T, K]):

#     def __init__(
#         self,
#         arm: T,
#         head: K
#         ) -> None:
#         self.arm = arm
#         self.head = head

# def test(x: T) -> T:
#     print(x, type(x))
#     return x

# test(1)
# test("2")