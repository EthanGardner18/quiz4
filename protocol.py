# Rewrite the above program using the protocol method
# [Name of the file should be protocol.py](1point)

from typing import Protocol
import os

class SIUE(Protocol):
    def save(self,data:str)->None:
        pass
    def load(self)->str:
        pass

class Student:
    def save(self, data: str) -> None:
        print("Student data saved:", data)

    def load(self) -> str:
        return "Student data loaded"

class Professor:
    def save(self, data: str) -> None:
        print("Professor data saved:", data)

    def load(self) -> str:
        return "Professor data loaded"

def main():
    student = Student()
    student.save("Computer Science Student")
    loaded_student_data = student.load()
    print("Action:", loaded_student_data)

    professor = Professor()
    professor.save("Computer Sciene Professor")
    loaded_professor_data = professor.load()
    print("Action:", loaded_professor_data)

if __name__ == '__main__':
    main()