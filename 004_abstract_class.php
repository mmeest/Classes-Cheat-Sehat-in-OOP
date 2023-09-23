<?php
abstract class Shape {
    // Abstract method that subclasses must implement
    public abstract function area();

    // Abstract method that subclasses must implement
    public abstract function perimeter();

    // Concrete method with implementation
    public function displayInfo() {
        echo "Area: " . $this->area() . "\n";
        echo "Perimeter: " . $this->perimeter() . "\n";
    }
}

class Circle extends Shape {
    private $radius;

    public function __construct($radius) {
        $this->radius = $radius;
    }

    public function area() {
        return M_PI * $this->radius * $this->radius;
    }

    public function perimeter() {
        return 2 * M_PI * $this->radius;
    }
}

class Rectangle extends Shape {
    private $width;
    private $height;

    public function __construct($width, $height) {
        $this->width = $width;
        $this->height = $height;
    }

    public function area() {
        return $this->width * $this->height;
    }

    public function perimeter() {
        return 2 * ($this->width + $this->height);
    }
}

// Create instances of concrete subclasses
$circle = new Circle(5);
$rectangle = new Rectangle(4, 6);

// Call methods and display information
$circle->displayInfo();
echo "\n";
$rectangle->displayInfo();
?>
