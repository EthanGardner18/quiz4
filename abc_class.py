# WAP to demonstrate ABC. Create a base class and inside of this base class there
# should be two abstract methods (use @bastractmethod decorator). This base class
# should be inherited by two other classes which will implement the methods inside of
# the base class. Come up with your own classes. Please do not create a class called
# vehicle and inherit it into motorbike and car.
# [Name of the file should be abc_class.py](1point)

from abc import ABC, abstractmethod
import os

class SIUE(ABC):

    @abstractmethod
    def save(self,data):
        pass
    @abstractmethod
    def load(self):
        pass

class Student(SIUE):
    def save(self,data):
        print("Student Data: ", data)
    def load(self):
        return "Student Data loaded"

class Professor(SIUE):
    def save(self,data):
        print("Professor Data: ", data)
    def load(self):
        return "Professor Data loaded"

def main():
    student = Student()
    student.save("computer science")
    load = student.load()
    print("Major: ", load)

    prof = Professor()
    prof.save("Dr. Das")
    loaded = prof.load()
    print("Professor: ", loaded)


if __name__ == '__main__':
    main()
