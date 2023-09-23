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

public class Main {
    public static void main(String[] args) {
        Person person1 = new Person("Alice", 30, "female");
        Person person2 = new Person("Bob", 25, "male");

        System.out.println(person1.name); // Output: Alice
        person2.introduce(); // Output: Hi, I'm Bob, 25 years old, and I am male.
    }
}
