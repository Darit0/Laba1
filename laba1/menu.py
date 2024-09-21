from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET

class Menu(ABC): #Интерфейс для всех будующих классов
    @abstractmethod
    def priceList(self):
        pass

    @abstractmethod
    def save_to_json(self, filename):
        pass

    @abstractmethod
    def save_to_xml(self, filename):
        pass

class HotDish(Menu):# Реализация горячих блюд
    def __init__(self):
        self.name = input("Введите название горячего блюда: ")
        while True:
            try: # Своя обработка
                self.price = float(input("Введите цену горячего блюда: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Пожалуйста, введите положительное число.")

        self.ingredients = input("Введите ингредиенты (через запятую): ").split(',')

    def priceList(self):
        print(f"\nГорячее блюдо: {self.name}")
        print(f"Цена: {self.price} руб.")
        print(f"Ингредиенты: {', '.join(self.ingredients)}")

class Drinks(Menu): #Реализация напитков
    def __init__(self):
        self.name = input("Введите название напитка: ")
        while True:
            try:
                self.price = float(input("Введите цену напитка: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Пожалуйста, введите положительное число.")

        self.volume = input("Введите объем (мл): ")

    def priceList(self):
        print(f"\nНапиток: {self.name}")
        print(f"Цена: {self.price} руб.")
        print(f"Объем: {self.volume}")