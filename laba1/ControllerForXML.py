import xml.etree.ElementTree as ET
class DisplayXml:

    # Функция для добавления отступов (pretty-print)
    def indent(elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                DisplayXml.indent(subelem, level + 1)
            if not subelem.tail or not subelem.tail.strip():
                subelem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def save_to_xml(data, filename):

        root = ET.Element('menu')

        hot_dishes = ET.SubElement(root, 'hot_dishes')
        for hot_dish in data['hot_dishes']:
            hot_dish_element = ET.SubElement(hot_dishes, 'hot_dish')
            for key, value in hot_dish.items():
                child = ET.SubElement(hot_dish_element, key)
                child.text = str(value)

        drinks = ET.SubElement(root, 'drinks')
        for drink in data['drinks']:
            drink_element = ET.SubElement(drinks, 'drink')
            for key, value in drink.items():
                child = ET.SubElement(drink_element, key)
                child.text = str(value)

        alcohols = ET.SubElement(root, 'alcohols')
        for alcohol in data['alcohols']:
            alcohol_element = ET.SubElement(alcohols, 'alcohol')
            for key, value in alcohol.items():
                child = ET.SubElement(alcohol_element, key)
                child.text = str(value)

        desserts = ET.SubElement(root, 'desserts')
        for dessert in data['desserts']:
            dessert_element = ET.SubElement(desserts, 'dessert')
            for key, value in dessert.items():
                child = ET.SubElement(dessert_element, key)
                child.text = str(value)

        salads = ET.SubElement(root, 'salads')
        for salad in data['salads']:
            salad_element = ET.SubElement(salads, 'salad')
            for key, value in salad.items():
                child = ET.SubElement(salad_element, key)
                child.text = str(value)

        bakeries = ET.SubElement(root, 'bakeries')
        for bakery in data['bakeries']:
            bakery_element = ET.SubElement(bakeries, 'bakery')
            for key, value in bakery.items():
                child = ET.SubElement(bakery_element, key)
                child.text = str(value)

        soups = ET.SubElement(root, 'soups')
        for soup in data['soups']:
            soup_element = ET.SubElement(soups, 'soup')
            for key, value in soup.items():
                child = ET.SubElement(soup_element, key)
                child.text = str(value)

        breakfastMeals = ET.SubElement(root, 'breakfastMeals')
        for breakfastMeal in data['breakfastMeals']:
            breakfastMeal_element = ET.SubElement(breakfastMeals, 'breakfastMeal')
            for key, value in breakfastMeal.items():
                child = ET.SubElement(breakfastMeal_element, key)
                child.text = str(value)

        DisplayXml.indent(root)
                # Создаем дерево XML и записываем его в файл
        try: #Обработка встроенной ошибки
            tree = ET.ElementTree(root)
            tree.write(filename, encoding='utf-8', xml_declaration=True)
            print(f"Все блюда успешно сохранены в файл '{filename}'")
        except IOError as e:
            print(f"Ошибка при записи в XML-файл: {str(e)}")

    #Загрузка блюд из файла
    def load_from_xml(filename):
        try: #Обработка встроенной ошибки
            tree = ET.parse(filename)
            root = tree.getroot()
        except FileNotFoundError:
            return {"hot_dishes": [], "drinks": [], "alcohols": [], "desserts": [],"salads": [],"bakeries": [],"soups": [],"breakfastMeals": []}

        data = {"hot_dishes": [], "drinks": [], "alcohols": [], "desserts": [],"salads": [],"bakeries": [],"soups": [],"breakfastMeals": []}

        # Загрузка горячих блюд
        hot_dishes = root.find('hot_dishes')
        if hot_dishes is not None:
            for dish in hot_dishes:
                dish_data = {}
                for child in dish:
                    dish_data[child.tag] = child.text
                data['hot_dishes'].append(dish_data)

        # Загрузка напитков
        drinks = root.find('drinks')
        if drinks is not None:
            for drink in drinks:
                drink_data = {}
                for child in drink:
                    drink_data[child.tag] = child.text
                data['drinks'].append(drink_data)

        # Загрузка алкогольных напитков
        alcohols = root.find('alcohols')
        if alcohols is not None:
            for alcohol in alcohols:
                alcohol_data = {}
                for child in alcohol:
                    alcohol_data[child.tag] = child.text
                data['alcohols'].append(alcohol_data)

        # Загрузка десертов
        desserts = root.find('desserts')
        if desserts is not None:
            for dessert in desserts:
                dessert_data = {}
                for child in dessert:
                    dessert_data[child.tag] = child.text
                data['desserts'].append(dessert_data)

        # Загрузка салатов
        salads = root.find('salads')
        if salads is not None:
            for salad in salads:
                salad_data = {}
                for child in salad:
                    salad_data[child.tag] = child.text
                data['salads'].append(salad_data)

        # Загрузка продуктов из выпечки
        bakery = root.find('bakeries')
        if bakery is not None:
            for product in bakery:
                product_data = {}
                for child in product:
                    product_data[child.tag] = child.text
                data['bakeries'].append(product_data)

        # Загрузка супов
        soups = root.find('soups')
        if soups is not None:
            for soup in soups:
                soup_data = {}
                for child in soup:
                    soup_data[child.tag] = child.text
                data['soups'].append(soup_data)

        # Загрузка завтраков
        breakfast_meals = root.find('breakfastMeals')
        if breakfast_meals is not None:
            for meal in breakfast_meals:
                meal_data = {}
                for child in meal:
                    meal_data[child.tag] = child.text
                data['breakfastMeals'].append(meal_data)

        return data

    #Добавление блюд
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
