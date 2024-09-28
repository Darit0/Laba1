import json

class DisplayJson:

    def save_to_json(data, filename):
        try:#Обработка встроенной ошибки
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Все блюда успешно сохранены в JSON-файл {filename}")
        except IOError as e:
            print(f"Ошибка при записи в JSON-файл: {str(e)}")

    def load_from_json(filename):
        try: #Обработка встроенной ошибки
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"hot_dishes": [], "drinks": [], "alcohols": [], "desserts": [],
                    "salads": [], "bakeries": [], "soups": [], "breakfastMeals": []}

        # Добавление блюд

    def add_hot_dish(data, hot_dish):
        data['hot_dishes'].append(hot_dish.to_dict())

    def add_drink(data, drink):
        data['drinks'].append(drink.to_dict())

    def add_alcohol(data, alcohol):
        data['alcohols'].append(alcohol.to_dict())

    def add_dessert(data, dessert):
        data['desserts'].append(dessert.to_dict())

    def add_salad(data, salad):
        data['salads'].append(salad.to_dict())

    def add_bakery(data, bakery):
        data['bakeries'].append(bakery.to_dict())

    def add_soup(data, soup):
        data['soups'].append(soup.to_dict())

    def add_breakfastMeal(data, breakfastMeal):
        data['breakfastMeals'].append(breakfastMeal.to_dict())

