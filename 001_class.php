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

// Creating objects (instances) of the Person class
$person1 = new Person("Alice", 30, "female");
$person2 = new Person("Bob", 25, "male");

// Accessing attributes and calling methods
echo $person1->name . "\n"; // Output: Alice
$person2->introduce();       // Output: Hi, I'm Bob, 25 years old, and I am male.
?>
