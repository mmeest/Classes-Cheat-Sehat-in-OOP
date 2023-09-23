class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I am {self.gender}.")

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I am a student with ID {self.student_id}.")

# Create instances of both Person and Student
person1 = Person("Alice", 30, "female")
student1 = Student("Bob", 25, "male", "S12345")

# Demonstrate polymorphism by calling the introduce method on both objects
person1.introduce()  # Output: Hi, I'm Alice, 30 years old, and I am female.
student1.introduce()  # Output: Hi, I'm Bob, 25 years old, and I am a student with ID S12345.



## In this Python example, we have the Person and Student classes. Both classes have an introduce method, but the Student class overrides the introduce method to provide a different implementation. This is an example of polymorphism, where objects of different classes can be treated as objects of a common base class (Person in this case) and can respond to the same method name (introduce) in a way that is appropriate for their specific class.

## When we call the introduce method on person1, it uses the implementation from the Person class, and when we call the introduce method on student1, it uses the overridden implementation from the Student class. This is the essence of polymorphism, where the behavior of a method can vary depending on the actual type of the object it is called on.