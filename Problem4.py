interface Fruit {
    void display();
}

class Apple implements Fruit {
    public void display() {
        System.out.println("This is Apple");
    }
}

class Mango implements Fruit {
    public void display() {
        System.out.println("This is Mango");
    }
}

class Orange implements Fruit {
    public void display() {
        System.out.println("This is Orange");
    }
}

class FruitFactory {
    public Fruit getFruit(String fruitType) {
        if (fruitType == null)
            return null;

        if (fruitType.equalsIgnoreCase("Apple"))
            return new Apple();
        else if (fruitType.equalsIgnoreCase("Mango"))
            return new Mango();
        else if (fruitType.equalsIgnoreCase("Orange"))
            return new Orange();

        return null;
    }
}

public class FactoryDemo {
    public static void main(String[] args) {
        FruitFactory factory = new FruitFactory();

        Fruit fruit1 = factory.getFruit("Apple");
        fruit1.display();

        Fruit fruit2 = factory.getFruit("Mango");
        fruit2.display();

        Fruit fruit3 = factory.getFruit("Orange");
        fruit3.display();
    }
}
