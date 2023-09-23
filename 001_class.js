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

const person1 = new Person("Alice", 30, "female");
const person2 = new Person("Bob", 25, "male");

console.log(person1.name); // Output: Alice
person2.introduce(); // Output: Hi, I'm Bob, 25 years old, and I am male.


