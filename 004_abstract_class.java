abstract class Shape {
    // Abstract method that subclasses must implement
    public abstract double area();

    // Abstract method that subclasses must implement
    public abstract double perimeter();

    // Concrete method with implementation
    public void displayInfo() {
        System.out.println("Area: " + area());
        System.out.println("Perimeter: " + perimeter());
    }
}

class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }
}

class Rectangle extends Shape {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public double area() {
        return width * height;
    }

    @Override
    public double perimeter() {
        return 2 * (width + height);
    }
}

public class Main {
    public static void main(String[] args) {
        // Create instances of concrete subclasses
        Shape circle = new Circle(5);
        Shape rectangle = new Rectangle(4, 6);

        // Call methods and display information
        circle.displayInfo();
        System.out.println();
        rectangle.displayInfo();
    }
}
