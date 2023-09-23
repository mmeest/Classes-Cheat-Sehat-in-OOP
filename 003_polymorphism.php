<?php
class Person {
    public $name;
    public $age;
    public $gender;

    public function __construct($name, $age, $gender) {
        $this->name = $name;
        $this->age = $age;
        $this->gender = $gender;
    }

    public function introduce() {
        echo "Hi, I'm {$this->name}, {$this->age} years old, and I am {$this->gender}.\n";
    }
}

class Student extends Person {
    public $studentId;

    public function __construct($name, $age, $gender, $studentId) {
        parent::__construct($name, $age, $gender);
        $this->studentId = $studentId;
    }

    public function introduce() {
        echo "Hi, I'm {$this->name}, {$this->age} years old, and I am a student with ID {$this->studentId}.\n";
    }
}

$person1 = new Person("Alice", 30, "female");
$student1 = new Student("Bob", 25, "male", "S12345");

// Demonstrate polymorphism by calling the introduce method on both objects
$person1->introduce();    // Output: Hi, I'm Alice, 30 years old, and I am female.
$student1->introduce();   // Output: Hi, I'm Bob, 25 years old, and I am a student with ID S12345.
?>
