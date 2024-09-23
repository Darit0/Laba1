from Controller import Display
from menu import HotDish, Drinks, Alcohol, Dessert, Salads, Soups, BreakfastMeal, Bakery


def main(): # Это основа - это база
    hot_dishes = []
    drinks = []
    alcohol = []
    desserts = []
    salads = []
    bakery = []
    soups = []
    breakfast_meals = []

    while True:
        Display.display_menu(hot_dishes + drinks + alcohol + desserts + salads + bakery + soups + breakfast_meals)

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
                       "11. Выход\n")

        if choice == '1':
            hot_dishes.append(Display.add_item(HotDish))
        elif choice == '2':
            drinks.append(Display.add_item(Drinks))
        elif choice == '3':
            alcohol.append(Display.add_item(Alcohol))
        elif choice == '4':
            desserts.append(Display.add_item(Dessert))
        elif choice == '5':
            salads.append(Display.add_item(Salads))
        elif choice == '6':
            bakery.append(Display.add_item(Bakery))
        elif choice == '7':
            soups.append(Display.add_item(Soups))
        elif choice == '8':
            breakfast_meals.append(Display.add_item(BreakfastMeal))
        elif choice == '9':
            Display.save_to_json("menu.json",
                                 hot_dishes + drinks + alcohol + desserts + salads + bakery + soups + breakfast_meals)
        elif choice == '10':
            Display.save_to_xml("menu.xml",
                                hot_dishes + drinks + alcohol + desserts + salads + bakery + soups + breakfast_meals)
        elif choice == '11':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()