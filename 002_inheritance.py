class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I am {self.gender}.")

# Create a subclass Student that inherits from Person
class Student(Person):
    def __init__(self, name, age, gender, student_id):
        # Call the constructor of the base class (Person) using super()
        super().__init__(name, age, gender)
        self.student_id = student_id

    # Add a new method specific to Student
    def study(self):
        print(f"{self.name} is studying.")

# Create instances of both Person and Student
person1 = Person("Alice", 30, "female")
student1 = Student("Bob", 25, "male", "S12345")

# Call methods from the base class
person1.introduce()  # Output: Hi, I'm Alice, 30 years old, and I am female.

# Call methods from the derived class
student1.introduce()  # Output: Hi, I'm Bob, 25 years old, and I am male.
student1.study()      # Output: Bob is studying.