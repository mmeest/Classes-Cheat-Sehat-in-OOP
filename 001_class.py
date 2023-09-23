class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I am {self.gender}.")

# Creating objects (instances) of the Person class
person1 = Person("Alice", 30, "female")
person2 = Person("Bob", 25, "male")

# Accessing attributes and calling methods
print(person1.name)  # Output: Alice
person2.introduce()  # Output: Hi, I'm Bob, 25 years old, and I am male.




