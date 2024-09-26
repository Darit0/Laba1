#Главный класс варианта
class Menu:
    # Конструктор
    def __init__(self, title, price):
        self.title = title
        self.price = price

    # Запись
    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price
        }
#Далее классы наследники
class HotDish(Menu):
    def __init__(self, title, price, ingredients):
        super().__init__(title, price)
        self.ingredients = ingredients

    def to_dict(self):
        hot_dish_dict = super().to_dict()
        hot_dish_dict.update({
            "ingredients": self.ingredients
        })
        return hot_dish_dict


class Drinks(Menu):
    def __init__(self, title, price, volume):
        super().__init__(title, price)
        self.volume = volume


    def to_dict(self):
        drinks_dict = super().to_dict()
        drinks_dict.update({
            "volume": self.volume,
        })
        return drinks_dict

class Alcohol(Menu):
    def __init__(self, title, price, percentage):
        super().__init__(title, price)
        self.percentage = percentage

    def to_dict(self):
        alcohol_dict = super().to_dict()
        alcohol_dict.update({
            "percentage": self.percentage
        })
        return alcohol_dict



class Dessert(Menu):
    def __init__(self, title, price, description):
        super().__init__(title, price)
        self.description = description


    def to_dict(self):
        dessert_dict = super().to_dict()
        dessert_dict.update({
            "description": self.description,
        })
        return dessert_dict

class Salad(Menu):
    def __init__(self, title, price, main_ingredient):
        super().__init__(title, price)
        self.main_ingredient = main_ingredient

    def to_dict(self):
        salads_dict = super().to_dict()
        salads_dict.update({
            "main_ingredient": self.main_ingredient
        })
        return salads_dict



class Bakery(Menu):
    def __init__(self, title, price, type):
        super().__init__(title, price)
        self.type = type


    def to_dict(self):
        bakery_dict = super().to_dict()
        bakery_dict.update({
            "type": self.type,
        })
        return bakery_dict

class Soup(Menu):
    def __init__(self, title, price, main_ingredient):
        super().__init__(title, price)
        self.main_ingredient = main_ingredient

    def to_dict(self):
        soups_dict = super().to_dict()
        soups_dict.update({
            "main_ingredient": self.main_ingredient
        })
        return soups_dict


class BreakfastMeal(Menu):
    def __init__(self, title, price, main_course,side_dish):
        super().__init__(title, price)
        self.main_course = main_course
        self.side_dish = side_dish

    def to_dict(self):
        breakfastMeal_dict = super().to_dict()
        breakfastMeal_dict.update({
            "main_course": self.main_course,
            "side_dish": self.side_dish
        })
        return breakfastMeal_dict