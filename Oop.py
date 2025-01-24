Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Assignment 1: Smartphone Class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, contact):
        print(f"Calling {contact} from {self.brand} {self.model}...")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.brand} {self.model}...")

    def check_battery(self):
        print(f"Battery life: {self.battery_life}%")

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, camera_quality):
        super().__init__(brand, model, storage, battery_life)
        self.camera_quality = camera_quality

    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} camera...")

# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass  # Abstract method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Main Program
if __name__ == "__main__":
    # Assignment 1 Example
    print("=== Smartphone Example ===")
    phone1 = Smartphone("Samsung", "Galaxy A12", 64, 85)
    phone1.make_call("John")
    phone1.install_app("WhatsApp")
    phone1.check_battery()

    phone2 = FlagshipPhone("Apple", "iPhone 15", 256, 90, "48MP")
    phone2.take_photo()
    phone2.make_call("Jane")

    # Activity 2 Example
    print("\n=== Polymorphism Example ===")
    car = Car()
    plane = Plane()

    car.move()
    plane.move()