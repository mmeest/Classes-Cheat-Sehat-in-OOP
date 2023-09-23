class Person {
    String name;
    int age;
    String gender;

    public Person(String name, int age, String gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    public void introduce() {
        System.out.println("Hi, I'm " + name + ", " + age + " years old, and I am " + gender + ".");
    }
}

class Student extends Person {
    String studentId;

    public Student(String name, int age, String gender, String studentId) {
        super(name, age, gender);
        this.studentId = studentId;
    }

    public void introduce() {
        System.out.println("Hi, I'm " + name + ", " + age + " years old, and I am a student with ID " + studentId + ".");
    }
}

public class Main {
    public static void main(String[] args) {
        Person person1 = new Person("Alice", 30, "female");
        Student student1 = new Student("Bob", 25, "male", "S12345");

        // Demonstrate polymorphism by calling the introduce method on both objects
        person1.introduce();    // Output: Hi, I'm Alice, 30 years old, and I am female.
        student1.introduce();   // Output: Hi, I'm Bob, 25 years old, and I am a student with ID S12345.
    }
}
