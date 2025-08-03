student = {"name" : "Arpit", "grades": (89,90,93,78,90)}



def average(sequence):
    return sum(sequence)/len(sequence)



print(average(student["grades"]))



# here average is pretty much a method which is standalone without context.

# it doesnt know what it takes as input, 

#but we may want to return the average for students as something like.
# student.average()

#OOP

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        # python turns an object into a easy to use string for users
        return f"name {self.name}, {self.grades} are the scores with average : {self.average()}"

    def __repr__(self):
        # python object for internal or debug usage, if we want to recreate an object during error conditions
        return f"<Student({self.name},{self.grades},{self.average()})>"

    def average(self):
        return sum(self.grades) / len(self.grades)


## when fucntion inside a class its called it method
student = Student("Arpit",(90,90,93,78,90))

print(student.name)
print(student.grades)
print(Student.average(student))
print(student.average())
print(f"student __str__ is : {student}")
print(f"student representation is : {student.__repr__()}")
print(f"student representation is : {repr(student)}")