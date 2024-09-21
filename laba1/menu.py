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

class HotDish(Menu):    # Реализация горячих блюд
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

    def save_to_json(self):
        return {
            "type": "hot_dish",
            "name": self.name,
            "price": self.price,
            "ingredients": self.ingredients
        }

    def save_to_xml(self):
        root = ET.Element("dish")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        ingredients = ET.SubElement(root, "ingredients")
        ingredients.text = ', '.join(self.ingredients)
        return root


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

    def save_to_json(self):
        return {
            "type": "drink",
            "name": self.name,
            "price": self.price,
            "volume": self.volume
        }

    def save_to_xml(self):
        root = ET.Element("drink")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        volume = ET.SubElement(root, "volume")
        volume.text = self.volume
        return root