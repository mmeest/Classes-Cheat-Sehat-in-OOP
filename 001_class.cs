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

    public void Introduce()
    {
        Console.WriteLine($"Hi, I'm {Name}, {Age} years old, and I am {Gender}.");
    }
}

class Program
{
    static void Main()
    {
        Person person1 = new Person("Alice", 30, "female");
        Person person2 = new Person("Bob", 25, "male");

        Console.WriteLine(person1.Name); // Output: Alice
        person2.Introduce(); // Output: Hi, I'm Bob, 25 years old, and I am male.
    }
}


