class Person {
    constructor(name, age, gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    introduce() {
        console.log(`Hi, I'm ${this.name}, ${this.age} years old, and I am ${this.gender}.`);
    }
}

class Student extends Person {
    constructor(name, age, gender, studentId) {
        super(name, age, gender);
        this.studentId = studentId;
    }

    study() {
        console.log(`${this.name} is studying.`);
    }
}

const person1 = new Person("Alice", 30, "female");
const student1 = new Student("Bob", 25, "male", "S12345");

person1.introduce();    // Output: Hi, I'm Alice, 30 years old, and I am female.
student1.introduce();   // Output: Hi, I'm Bob, 25 years old, and I am male.
student1.study();       // Output: Bob is studying.