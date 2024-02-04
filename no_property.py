# Extend the above program (program-6) by removing the @property decorator and
# simply use a function. Consult my codes from the class. Come up with a different
# program. [Name of the file should be no_property.py] (1point)

class classes:
    def __init__(self, name, courseNum):
        self._name = name
        self._courseNum = courseNum

    def get_name(self):
        return self._name

    def get_courseNum(self):
        return self._courseNum

def main():
    calculus1 = classes(name="Calculus 1", courseNum = 150)
    softwareEng = classes(name="SoftWare Engineering", courseNum = 325)
    
    print(f"Student 1 - Name: {calculus1.get_name()}, Age: {calculus1.get_courseNum()}")
    print(f"Student 2 - Name: {softwareEng.get_name()}, Age: {softwareEng.get_courseNum()}")


if __name__ == "__main__":
    main()
