# Define a parent class called "Animal"
class Animal:
  def __init__(self, name):
    self.name = name

  def sound(self):
    print("The animal makes a sound.")

# Define a child class called "Dog" that inherits from Animal
class Dog(Animal):
  def __init__(self,name, breed):
    super().__init__(name)  # Call the parent class's constructor
    self.breed = breed

  

# Create an object called "my_dog" from the Dog class
my_dog = Dog("Fido", "Golden Retriever")

# Access the object's properties and behaviors
print(my_dog.name, my_dog.breed)
# Output: Fido
my_dog.sound()  # Output: The dog barks.