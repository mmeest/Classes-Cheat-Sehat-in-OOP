// Define a "Shape" interface-like object
const Shape = {
    area() {
        throw new Error("Method 'area' must be implemented in subclasses.");
    },
    perimeter() {
        throw new Error("Method 'perimeter' must be implemented in subclasses.");
    },
};

// Create a constructor function for "Circle"
function Circle(radius) {
    this.radius = radius;
}

// Inherit from the "Shape" object
Circle.prototype = Object.create(Shape);

// Implement the "area" method for "Circle"
Circle.prototype.area = function () {
    return Math.PI * this.radius * this.radius;
};

// Implement the "perimeter" method for "Circle"
Circle.prototype.perimeter = function () {
    return 2 * Math.PI * this.radius;
};

// Create a constructor function for "Rectangle"
function Rectangle(width, height) {
    this.width = width;
    this.height = height;
}

// Inherit from the "Shape" object
Rectangle.prototype = Object.create(Shape);

// Implement the "area" method for "Rectangle"
Rectangle.prototype.area = function () {
    return this.width * this.height;
};

// Implement the "perimeter" method for "Rectangle"
Rectangle.prototype.perimeter = function () {
    return 2 * (this.width + this.height);
};

// Create instances of "Circle" and "Rectangle"
const circle = new Circle(5);
const rectangle = new Rectangle(4, 6);

// Call methods and display information
console.log("Circle Area:", circle.area());
console.log("Circle Perimeter:", circle.perimeter());
console.log();
console.log("Rectangle Area:", rectangle.area());
console.log("Rectangle Perimeter:", rectangle.perimeter());
