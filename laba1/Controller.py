import json
import xml.etree.ElementTree as ET
class Display:
    @staticmethod
    def display_menu(menu_items):
        for item in menu_items:
            item.priceList()

    @staticmethod
    def add_item(item_class):
        item = item_class()
        # Здесь можно добавить дополнительную логику для отображения информации о добавленном элементе
        print(f"\nДобавлено: {item.name}")
        return item

    @staticmethod
    def save_to_json(filename, menu_items):
        menu_data = []
        for item in menu_items:
            menu_data.append(item.save_to_json())

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(menu_data, f, ensure_ascii=False, indent=4)
            print(f"Все блюда успешно сохранены в JSON-файл {filename}")
        except IOError as e:
            print(f"Ошибка при записи в JSON-файл: {str(e)}")

    @staticmethod
    def save_to_xml(filename, menu_items):
        root = ET.Element("menu")
        for item in menu_items:
            item_element = item.save_to_xml()
            root.append(item_element)

        try:
            tree = ET.ElementTree(root)
            tree.write(filename, encoding="unicode", xml_declaration=True)
            print(f"Все блюда успешно сохранены в XML-файл {filename}")
        except IOError as e:
            print(f"Ошибка при записи в XML-файл: {str(e)}")
