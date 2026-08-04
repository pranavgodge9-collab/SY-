import java.util.ArrayList;
import java.util.List;

interface Observer {
    void update(float temperature);
}

class DisplayDevice implements Observer {
    private String name;

    public DisplayDevice(String name) {
        this.name = name;
    }

    public void update(float temperature) {
        System.out.println(name + " received temperature update: " + temperature + "°C");
    }
}

class WeatherStation {
    private List<Observer> observers = new ArrayList<>();
    private float temperature;

    public void registerObserver(Observer observer) {
        observers.add(observer);
    }

    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    public void setTemperature(float temperature) {
        this.temperature = temperature;
        notifyObservers();
    }

    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(temperature);
        }
    }
}

public class ObserverDemo {
    public static void main(String[] args) {
        WeatherStation station = new WeatherStation();

        DisplayDevice mobile = new DisplayDevice("Mobile Display");
        DisplayDevice lcd = new DisplayDevice("LCD Display");
        DisplayDevice led = new DisplayDevice("LED Display");

        station.registerObserver(mobile);
        station.registerObserver(lcd);
        station.registerObserver(led);

        System.out.println("Temperature changed to 30°C");
        station.setTemperature(30);

        System.out.println();

        System.out.println("Temperature changed to 35°C");
        station.setTemperature(35);
    }
}
