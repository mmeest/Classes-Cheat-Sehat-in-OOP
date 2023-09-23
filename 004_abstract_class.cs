using System;

// Define an abstract class
public abstract class Shape
{
    // Abstract method that subclasses must implement
    public abstract double Area();

    // Abstract method that subclasses must implement
    public abstract double Perimeter();

    // Concrete method with implementation
    public void DisplayInfo()
    {
        Console.WriteLine($"Area: {Area()}");
        Console.WriteLine($"Perimeter: {Perimeter()}");
    }
}

// Create a concrete subclass
public class Circle : Shape
{
    private double radius;

    public Circle(double radius)
    {
        this.radius = radius;
    }

    public override double Area()
    {
        return Math.PI * radius * radius;
    }

    public override double Perimeter()
    {
        return 2 * Math.PI * radius;
    }
}

// Create a concrete subclass
public class Rectangle : Shape
{
    private double width;
    private double height;

    public Rectangle(double width, double height)
    {
        this.width = width;
        this.height = height;
    }

    public override double Area()
    {
        return width * height;
    }

    public override double Perimeter()
    {
        return 2 * (width + height);
    }
}

class Program
{
    static void Main()
    {
        // Create instances of concrete subclasses
        Shape circle = new Circle(5);
        Shape rectangle = new Rectangle(4, 6);

        // Call methods and display information
        circle.DisplayInfo();
        Console.WriteLine();
        rectangle.DisplayInfo();
    }
}
