import json
import xml.etree.ElementTree as ET
from menu import HotDish, Drinks


def main(): # Это основа - это база
    hot_dishes = []
    drinks = []

    def add_hot_dish():
        dish = HotDish()
        hot_dishes.append(dish)
        print(f"\nГорячее блюдо '{dish.name}' добавлено в меню.")

    def add_drink():
        drink = Drinks()
        drinks.append(drink)
        print(f"\nНапиток '{drink.name}' добавлен в меню.")

    def display_menu():
        print("\nТекущее меню:")
        for i, dish in enumerate(hot_dishes, start=1):
            print(f"\n{i}. Горячее блюдо")
            dish.priceList()
        for i, drink in enumerate(drinks, start=len(hot_dishes) + 1):
            print(f"\n{i}. Напиток")
            drink.priceList()

    def save_to_json(filename):
        menu_data = {
            'hot_dishes': [dish.__dict__ for dish in hot_dishes],
            'drinks': [drink.__dict__ for drink in drinks]
        }
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(menu_data, f, ensure_ascii=False, indent=4)
            print(f"Данные успешно сохранены в файл {filename}")
        except IOError as e:
            print(f"Ошибка при записи в JSON-файл: {str(e)}")

    def save_to_xml(filename):
        root = ET.Element("menu")

        hot_dishes_element = ET.SubElement(root, "hot_dishes")
        for dish in hot_dishes:
            item = ET.SubElement(hot_dishes_element, "dish")
            for attr_name, value in dish.__dict__.items():
                if not attr_name.startswith('__'):
                    child = ET.SubElement(item, attr_name)
                    child.text = str(value)

        drinks_element = ET.SubElement(root, "drinks")
        for drink in drinks:
            item = ET.SubElement(drinks_element, "drink")
            for attr_name, value in drink.__dict__.items():
                if not attr_name.startswith('__'):
                    child = ET.SubElement(item, attr_name)
                    child.text = str(value)

        try:
            tree = ET.ElementTree(root)
            tree.write(filename, encoding="unicode", xml_declaration=True)
            print(f"Данные успешно сохранены в файл {filename}")
        except IOError as e:
            print(f"Ошибка при записи в XML-файл: {str(e)}")

    add_hot_dish()#Добавление заполненных данных
    add_drink()

    while True:
        display_menu()
        choice = input(
            "\nВыберите действие:\n1. Добавить горячее блюдо\n"
            "2. Добавить напиток\n3. Сохранить в JSON\n"
            "4. Сохранить в XML\n5. Выход\n")

        if choice == '1':
            add_hot_dish()
        elif choice == '2':
            add_drink()
        elif choice == '3':
            save_to_json("menu.json")
        elif choice == '4':
            save_to_xml("menu.xml")
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()