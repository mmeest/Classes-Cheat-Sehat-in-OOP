# Classes-Cheat-Sehat-in-OOP
Classes Cheat Sheat in OOP

## Contetns
- [Attributes](#attributes)
- [Methods](#methods)
- [Constructor](#constructor)
- [Instance](#instance)
- [Accessing attributes and calling methods](#accessing-attributes-and-calling-methods)
- [Inheritance](#inheritance)
- [Polymorphism](#polymorphism)
- [Method overriding](#method-overriding)
- [Prevent method overriding](#prevent-method-overriding)
- [Abstract class](#abstract-class)

## Attributes
Attributes or Properties are the data members or variables that store information about the object. Attributes represent the characteristics or state of the object. For example, if you're creating a class to represent a "Person," attributes might include name, age, and gender.

Example:

| Language | Attribute |
|-|-|
| Python | self.name = name |
| C# (public field in class without constructor)| public string Name { get; set; } |
| JavaScript | this.name = name; |
| JAVA | this.name = name; |
| PHP | $this->name = $name; |
        

## Methods
Methods are functions defined within the class that define the behaviors or actions that objects of the class can perform. For example, for the "Person" class, you might have methods like speak(), walk(), or eat().

Example:

| Language | |
|-|-|
| Python | def introduce(self): |
| C# | public Person(string name, int age, string gender) { ... } |
| JavaScript | introduce() { ... } |
| JAVA | public void introduce() { ... } |
| PHP | public function introduce() { ... } |

## Constructor
Constructor is a special method that gets called when you create a new object from a class. It typically initializes the object's attributes. In many programming languages, the constructor method is named after the class itself (e.g., __init__ in Python).

Example:

| Language | Creating Constructor |
|-|-|
| Python | def __init__(self, name, age, gender): |
| C# | C# does not need a constructor. Class level variables can be defined on public fields |
| JavaScript | constructor(name, age, gender) { ... } |
| JAVA | public Person(String name, int age, String gender) { ... } |
| PHP | public function __construct($name, $age, $gender) { ... } |

## Instance

Example:

| Language | Defining an instance |
|-|-|
| Python | person1 = Person("Alice", 30, "female") |
| C# inside Program/Main | Person person1 = new Person("Alice", 30, "female"); |
| JavaScript | const person1 = new Person("Alice", 30, "female"); |
| JAVA from 'Main' class | Person person1 = new Person("Alice", 30, "female"); |
| PHP | $person1 = new Person("Alice", 30, "female"); |

## Accessing attributes and calling methods

Accessing attribute example:

| Language | Accessing attribute |
|-|-|
| Python | print(person1.name) |
| C# | Console.WriteLine(person1.Name); |
| JavaScript | console.log(person1.name); |
| JAVA | System.out.println(person1.name); |
| PHP | echo $person1->name; |

Method calling example:

| Language | Accessing attribute |
|-|-|
| Python | person2.introduce() |
| C# | person2.Introduce(); |
| JavaScript | person2.introduce(); |
| JAVA | person2.introduce(); |
| PHP | $person2->introduce(); |

## Inheritance

## Polymorphism

## Method overriding
Method overriding is a fundamental concept in object-oriented programming (OOP) that allows a subclass to provide a specific implementation of a method that is already defined in its superclass (or parent class). This enables polymorphism, where objects of different classes can respond to the same method name in a way that is appropriate for their specific class. Here's an explanation of method overriding:

  1.  Inheritance: Method overriding is closely related to inheritance. Inheritance is the mechanism by which one class (subclass or derived class) inherits the attributes and methods of another class (superclass or base class). The subclass can extend or modify the behavior of the superclass.

  2.  Method Signature: For method overriding to occur, the method in the subclass must have the same name, return type, and parameter list (method signature) as the method in the superclass. The method signature serves as a contract between the superclass and its subclasses.

  3.  @Override Annotation (Java): In languages like Java, you can use the @Override annotation to explicitly indicate that a method in a subclass is intended to override a method in the superclass. This annotation helps catch errors at compile-time if there's a mismatch in method signatures.

  4.  Runtime Polymorphism: Method overriding enables runtime polymorphism, which means that the appropriate method implementation is determined at runtime based on the actual object's type. This allows you to write more generic code that can work with objects of various subclasses.

  5.  Super Keyword (Optional): In many languages, including Java and Python, you can use the super keyword to call the superclass's version of the overridden method from within the subclass's method. This is useful when you want to extend the behavior of the superclass's method.

Here's an example in Java to illustrate method overriding:

```
class Animal {
    void makeSound() {
        System.out.println("The animal makes a generic sound.");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("The dog barks.");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog(); // Polymorphism
        animal.makeSound(); // Output: The dog barks.
    }
}
```

In this example, we have a superclass Animal with a method makeSound(), and a subclass Dog that overrides the makeSound() method. When we create a Dog object and assign it to an Animal reference, we can call makeSound(). The overridden method in the Dog class is invoked, demonstrating method overriding and polymorphism.

## Prevent method overriding
In object-oriented programming, you can prevent method overriding (also known as method sealing or method finalization) by using language-specific mechanisms or keywords that restrict a method from being overridden in subclasses. Below, I'll explain how to prevent method overriding in Java and C#.

In Java:

In Java, you can prevent method overriding by using the final keyword. When you declare a method as final in a class, it becomes a sealed method, and subclasses are not allowed to override it. Here's an example:

```
class Parent {
    final void finalMethod() {
        System.out.println("This method cannot be overridden.");
    }
}

class Child extends Parent {
    // This will result in a compilation error since you can't override a final method.
    // void finalMethod() { }
}

public class Main {
    public static void main(String[] args) {
        Parent parent = new Parent();
        parent.finalMethod(); // Output: This method cannot be overridden.
    }
}
```

In object-oriented programming, you can prevent method overriding (also known as method sealing or method finalization) by using language-specific mechanisms or keywords that restrict a method from being overridden in subclasses. Below, I'll explain how to prevent method overriding in Java and C#.

In Java:

In Java, you can prevent method overriding by using the final keyword. When you declare a method as final in a class, it becomes a sealed method, and subclasses are not allowed to override it. Here's an example:

java

class Parent {
    final void finalMethod() {
        System.out.println("This method cannot be overridden.");
    }
}

class Child extends Parent {
    // This will result in a compilation error since you can't override a final method.
    // void finalMethod() { }
}

public class Main {
    public static void main(String[] args) {
        Parent parent = new Parent();
        parent.finalMethod(); // Output: This method cannot be overridden.
    }
}

In this example, the finalMethod() in the Parent class is declared as final, so when we try to override it in the Child class, it results in a compilation error.

In C#:

In C#, you can prevent method overriding by using the sealed keyword. When you declare a method as sealed in a class, it becomes a sealed method, and subclasses are not allowed to override it. Here's an example:

```
class Parent
{
    public sealed void SealedMethod()
    {
        Console.WriteLine("This method cannot be overridden.");
    }
}

class Child : Parent
{
    // This will result in a compilation error since you can't override a sealed method.
    // public override void SealedMethod() { }
}

class Program
{
    static void Main()
    {
        Parent parent = new Parent();
        parent.SealedMethod(); // Output: This method cannot be overridden.
    }
}
```

In this C# example, the SealedMethod() in the Parent class is declared as sealed, so when we try to override it in the Child class, it results in a compilation error.

Using final or sealed is a way to enforce that certain methods in a class hierarchy should not be modified in subclasses, which can be useful in maintaining the integrity of your code when designing class hierarchies.

## Abstract class

An abstract class is a class that cannot be instantiated and is meant to be subclassed. It may contain abstract methods, which are methods that have no implementation in the abstract class and must be implemented in any concrete subclass.
