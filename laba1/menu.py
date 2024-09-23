from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET

class Menu():    # Интерфейс для всех будующих классов

    def __init__(self):
        self.name = input("Ввод продукта")
        self.price = float(input("enter price"))

    @abstractmethod
    def priceList(self):
        pass

    @abstractmethod
    def save_to_json(self, filename):
        pass

    @abstractmethod
    def save_to_xml(self, filename):
        pass

class HotDish(Menu):   # Реализация горячих блюд
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

class Alcohol(Menu):
    def __init__(self):
        self.name = input("Введите название алкогольного напитка: ")
        while True:
            try:
                self.price = float(input("Введите цену алкогольного напитка: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Пожалуйста, введите положительное число.")

        self.alcohol_percentage = input("Введите процент содержания алкоголя: ")

    def priceList(self):
        print(f"\nАлкогольный напиток: {self.name}")
        print(f"Цена: {self.price} руб.")
        print(f"Процент алкоголя: {self.alcohol_percentage}")

    def save_to_json(self):
        return {
            "type": "alcohol",
            "name": self.name,
            "price": self.price,
            "alcohol_percentage": self.alcohol_percentage
        }

    def save_to_xml(self):
        root = ET.Element("alcohol")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        alcohol_percentage = ET.SubElement(root, "alcohol_percentage")
        alcohol_percentage.text = self.alcohol_percentage
        return root

class Dessert(Menu):
    def __init__(self):
        self.name = input("Введите название десерта: ")
        while True:
            try:
                self.price = float(input("Введите цену десерта: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Пожалуйста, введите положительное число.")

        self.description = input("Введите описание десерта: ")

    def priceList(self):
        print(f"\nДесерт: {self.name}")
        print(f"Цена: {self.price} руб.")
        print(f"Описание: {self.description}")

    def save_to_json(self):
        return {
            "type": "dessert",
            "name": self.name,
            "price": self.price,
            "description": self.description
        }

    def save_to_xml(self):
        root = ET.Element("dessert")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        description = ET.SubElement(root, "description")
        description.text = self.description
        return root

class Salads(Menu):
    def __init__(self):
        self.name = input("Введите название салата: ")
        while True:
            try:
                self.price = float(input("Введите цену салата: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Пожалуйста, введите положительное число.")

        self.main_ingredient = input("Введите основной ингредиент салата: ")

    def priceList(self):
        print(f"\nСалат: {self.name}")
        print(f"Цена: {self.price} руб.")
        print(f"Основной ингредиент: {self.main_ingredient}")

    def save_to_json(self):
        return {
            "type": "salad",
            "name": self.name,
            "price": self.price,
            "main_ingredient": self.main_ingredient
        }

    def save_to_xml(self):
        root = ET.Element("salad")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        main_ingredient = ET.SubElement(root, "main_ingredient")
        main_ingredient.text = self.main_ingredient
        return root

class Bakery(Menu):
    def __init__(self):
        self.name = input("Введите название продукта из кондитерской: ")
        while True:
            try:
                self.price = float(input("Введите цену продукта из кондитерской: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Пожалуйста, введите положительное число.")

        self.type = input("Введите тип продукта (печенье, кекс, торт): ")

    def priceList(self):
        print(f"\nПродукт из кондитерской: {self.name}")
        print(f"Цена: {self.price} руб.")
        print(f"Тип: {self.type}")

    def save_to_json(self):
        return {
            "type": "bakery",
            "name": self.name,
            "price": self.price,
            "type": self.type
        }

    def save_to_xml(self):
        root = ET.Element("bakery")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        type = ET.SubElement(root, "type")
        type.text = self.type
        return root

class Soups(Menu):
    def __init__(self):
        self.name = input("Введите название супа: ")
        while True:
            try:
                self.price = float(input("Введите цену супа: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Пожалуйста, введите положительное число.")

        self.main_ingredient = input("Введите основной ингредиент супа: ")

    def priceList(self):
        print(f"\nСуп: {self.name}")
        print(f"Цена: {self.price} руб.")
        print(f"Основной ингредиент: {self.main_ingredient}")

    def save_to_json(self):
        return {
            "type": "soup",
            "name": self.name,
            "price": self.price,
            "main_ingredient": self.main_ingredient
        }

    def save_to_xml(self):
        root = ET.Element("soup")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        main_ingredient = ET.SubElement(root, "main_ingredient")
        main_ingredient.text = self.main_ingredient
        return root

class BreakfastMeal(Menu):
    def __init__(self):
        self.name = input("Введите название завтрака: ")
        while True:
            try:
                self.price = float(input("Введите цену завтрака: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Пожалуйста, введите положительное число.")

        self.main_course = input("Введите основное блюдо: ")
        self.side_dish = input("Введите гарнир: ")

    def priceList(self):
        print(f"\nЗавтрак: {self.name}")
        print(f"Цена: {self.price} руб.")
        print(f"Основное блюдо: {self.main_course}")
        print(f"Гарнир: {self.side_dish}")

    def save_to_json(self):
        return {
            "type": "breakfast_meal",
            "name": self.name,
            "price": self.price,
            "main_course": self.main_course,
            "side_dish": self.side_dish
        }

    def save_to_xml(self):
        root = ET.Element("breakfast_meal")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        main_course = ET.SubElement(root, "main_course")
        main_course.text = self.main_course
        side_dish = ET.SubElement(root, "side_dish")
        side_dish.text = self.side_dish
        return root
