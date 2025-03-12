public class overs {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Cat cat = new Cat();

        dog.eat();  
        dog.bark(); 
        cat.eat();  
        cat.meow(); 
    }
}
class Animal {
    void eat() {
        System.out.println("This animal eats food.");
    }
}

class Dog extends Animal {
    @Override
    void eat(){
        System.out.println("Dog is eating");
    }
    void bark() {
        System.out.println("The dog barks.");
    }
}

class Cat extends Animal {
    @Override
    void eat(){
        System.out.println("Cat is eating");
    }
    void meow() {
        System.out.println("The cat meows.");
    }
}

