# WAP a program that will demonstrate the @property decorator.
# [Name of the file should be property.py](1point)

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

def main():
    student1 = Student(name="Ethan", age=20)
    student2 = Student(name="Das", age=30)
    
    print(f"Student 1 - Name: {student1.name}, Age: {student1.age}")
    print(f"Student 2 - Name: {student2.name}, Age: {student2.age}")

if __name__ == "__main__":
    main()