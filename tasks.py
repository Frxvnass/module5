from typing import NamedTuple
from dataclasses import dataclass

class Student(NamedTuple):
    name: str
    age: int
    grade: float

s1 = Student("muslima", 18,88.0)
print(s1.name)
print(s1.age)
print(s1.grade)

@dataclass
class Student2:
    name: str
    age: int
    grade: float

s2 = Student2("muslima", 18,88.0)
s2.grade = 91.5
print(s2.name)
print(s2.age)
print(s2.grade)
