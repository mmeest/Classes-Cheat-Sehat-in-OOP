using System;

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Gender { get; set; }

    public Person(string name, int age, string gender)
    {
        Name = name;
        Age = age;
        Gender = gender;
    }

    public virtual void Introduce()
    {
        Console.WriteLine($"Hi, I'm {Name}, {Age} years old, and I am {Gender}.");
    }
}

class Student : Person
{
    public string StudentId { get; set; }

    public Student(string name, int age, string gender, string studentId)
        : base(name, age, gender)
    {
        StudentId = studentId;
    }

    public override void Introduce()
    {
        Console.WriteLine($"Hi, I'm {Name}, {Age} years old, and I am a student with ID {StudentId}.");
    }
}

class Program
{
    static void Main()
    {
        Person person1 = new Person("Alice", 30, "female");
        Student student1 = new Student("Bob", 25, "male", "S12345");

        // Demonstrate polymorphism by calling the Introduce method on both objects
        person1.Introduce();    // Output: Hi, I'm Alice, 30 years old, and I am female.
        student1.Introduce();   // Output: Hi, I'm Bob, 25 years old, and I am a student with ID S12345.
    }
}
