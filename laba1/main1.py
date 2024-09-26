from ControllerForJSON import DisplayJson
from ControllerForXML import DisplayXml
from menu import HotDish, Drinks, Alcohol, Dessert, Salad, Soup, BreakfastMeal, Bakery

def get_good_number(x): # Валидация + обработка своей ошибки
    while True:
        try:
            price = int(input(x))
            if price <= 0:
                raise ValueError
            return price
            break
        except ValueError:
            print("Пожалуйста, введите положительное число.")

# Вывод информации
def print_data(data, file_format):
    if file_format == 'json':
        print("\nДанные из JSON:")
    elif file_format == 'xml':
        print("\nДанные из XML:")

    # Вывод горячих блюд
    print("\nГорячие блюда:")
    for dish in data['hot_dishes']:
        print(f"Название: {dish['title']}, Цена: {dish['price']} руб., Ингредиенты: {dish['ingredients']}")

    # Вывод напитков
    print("\nНапитки:")
    for drink in data['drinks']:
        print(f"Название: {drink['title']}, Цена: {drink['price']} руб., Объем: {drink['volume']} мл.")

    # Вывод алкогольных напитков
    print("\nАлкогольные напитки:")
    for alcohol in data['alcohols']:
        print(
            f"Название: {alcohol['title']}, Цена: {alcohol['price']} руб., Процент алкоголя: {alcohol['percentage']}%")

    # Вывод десертов
    print("\nДесерты:")
    for dessert in data['desserts']:
        print(f"Название: {dessert['title']}, Цена: {dessert['price']} руб., Описание: {dessert['description']}")

    # Вывод салатов
    print("\nСалаты:")
    for salad in data['salads']:
        print(
            f"Название: {salad['title']}, Цена: {salad['price']} руб., Основной ингредиент: {salad['main_ingredient']}")

    # Вывод продуктов из выпечки
    print("\nПродукты из выпечки:")
    for bakery in data['bakeries']:
        print(f"Название: {bakery['title']}, Цена: {bakery['price']} руб., Тип: {bakery['type']}")

    # Вывод супов
    print("\nСупы:")
    for soup in data['soups']:
        print(
            f"Название: {soup['title']}, Цена: {soup['price']} руб., Основной ингредиент: {soup['main_ingredient']}")

    # Вывод завтраков
    print("\nЗавтраки:")
    for breakfast_meal in data['breakfastMeals']:
        print(f"Название: {breakfast_meal['title']}, Цена: {breakfast_meal['price']} руб.")
        print(f"Основное блюдо: {breakfast_meal['main_course']}")
        print(f"Дополнительно: {breakfast_meal['side_dish']}")


def main(): # Это основа - это база

    dataFromJson = DisplayJson.load_from_json("menu.json") # читаем и закидываем туда данные
    dataFromXml = DisplayXml.load_from_xml("menu.xml")

    while True:

        choice = input("\nВыберите действие:\n"
                        "1. Добавить горячее блюдо\n"
                        "2. Добавить напиток\n"
                        "3. Добавить алкогольный напиток\n"
                        "4. Добавить десерт\n"
                        "5. Добавить салат\n"
                        "6. Добавить продукт из кондитерской\n"
                        "7. Добавить суп\n"
                        "8. Добавить завтрак\n"
                        "9. Сохранить в JSON\n"
                        "10. Сохранить в XML\n"
                        "11. Читать из JSON\n"
                        "12. Читать из XML\n"
                        "13. Выход\n")

        if choice == '1':
            title = input("Введите название Горячего блюда: ")
            price = get_good_number("Введите цену: ")
            ingredients = input("Введите ингредиенты: ")
            hot_dish = HotDish(title, price, ingredients)
            DisplayJson.add_hot_dish(dataFromJson, hot_dish)
            DisplayXml.add_hot_dish(dataFromXml, hot_dish)
        elif choice == '2':
            title = input("Введите название Напитка: ")
            price = get_good_number("Введите цену: ")
            volume = get_good_number("Введите объем: ")
            drink = Drinks(title, price, volume)
            DisplayJson.add_drink(dataFromJson, drink)
            DisplayXml.add_drink(dataFromXml, drink)
        elif choice == '3':
            title = input("Введите название Алкоголя: ")
            price = get_good_number("Введите цену: ")
            percentage = get_good_number("Введите градусы: ")
            alcohol = Drinks(title, price, percentage)
            DisplayJson.add_alcohol(dataFromJson, alcohol)
            DisplayXml.add_alcohol(dataFromXml, alcohol)
        elif choice == '4':
            title = input("Введите название Десерта: ")
            price = get_good_number("Введите цену: ")
            description = input("Введите описание: ")
            dessert = Dessert(title, price, description)
            DisplayJson.add_dessert(dataFromJson, dessert)
            DisplayXml.add_dessert(dataFromXml, dessert)
        elif choice == '5':
            title = input("Введите название Салата: ")
            price = get_good_number("Введите цену: ")
            main_ingredient = input("Введите Главный ингредиент: ")
            salad = Salad(title, price, main_ingredient)
            DisplayJson.add_salad(dataFromJson, salad)
            DisplayXml.add_salad(dataFromXml, salad)
        elif choice == '6':
            title = input("Введите название Выпечки: ")
            price = get_good_number("Введите цену: ")
            type = input("Введите Тип продукта(сладкое / не сладкое): ")
            bakery = Bakery(title, price, type)
            DisplayJson.add_bakery(dataFromJson, bakery)
            DisplayXml.add_bakery(dataFromXml, bakery)
        elif choice == '7':
            title = input("Введите название Супа: ")
            price = get_good_number("Введите цену: ")
            main_ingredient = input("Введите Главный ингредиент: ")
            soup = Soup(title, price, main_ingredient)
            DisplayJson.add_soup(dataFromJson, soup)
            DisplayXml.add_soup(dataFromXml, soup)
        elif choice == '8':
            title = input("Введите название Завтрака: ")
            price = get_good_number("Введите цену: ")
            main_course = input("Введите Главное блюдое: ")
            side_dish = input("Введите Второе: ")
            breakFastMeal = BreakfastMeal(title, price, main_course, side_dish)
            DisplayJson.add_breakfastMeal(dataFromJson, breakFastMeal)
            DisplayXml.add_breakfastMeal(dataFromXml, breakFastMeal)
        elif choice == '9':
            DisplayJson.save_to_json(dataFromJson, "menu.json")
            print(f"Данные сохранены в menu.json ")
        elif choice == '10':
            DisplayXml.save_to_xml(dataFromXml, "menu.xml")
            print(f"Данные сохранены в menu.xml ")
        elif choice == '11':
            print_data(dataFromJson, 'json')
        elif choice == '12':
            print_data(dataFromXml, 'xml')

if __name__ == "__main__":
    main()