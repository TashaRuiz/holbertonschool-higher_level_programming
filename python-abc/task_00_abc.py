#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """abstract method must be implemented by a subclasses"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """dog subclass that inherreted drom the animal class"""
    def sound(self):
        return ("Bark")

class Cat(Animal):
    """cat subclass that inherreted drom the animal class"""
    def sound(self):
        return("Meow")
