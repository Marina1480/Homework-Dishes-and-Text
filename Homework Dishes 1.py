class CookBook():
    def cook_book_read(self, file):
        self.cook_book = {}
        with open(file, 'r', encoding="utf-8") as file:
            for line in file:
                ingredients = []
                dish_name = line.strip()
                ingredients_number = int(file.readline().strip())
                for ingredient in range(ingredients_number):
                    name, count, measure = file.readline().strip().split('|')
                    ingredients.append({'ingredient_name': name.strip(), 'quantity': int(count),
                                        'measure': measure.strip()})
                file.readline()
                self.cook_book[dish_name] = ingredients
        print(self.cook_book)
        return self.cook_book
    def get_shop_list_by_dishes(self, dishes, person_count):
        getattr(self, 'cook_book', '')
        shop_list = {}
        for dish in dishes:
            if dish in self.cook_book.keys():
                for i in self.cook_book.get(dish):
                    dict_i = {}
                    dict_i['measure'] = i['measure']
                    if i['ingredient_name'] not in shop_list.keys():
                        dict_i['quantity'] = i['quantity'] * person_count
                    else:
                        dict_i['quantity'] += i['quantity'] * person_count
                    shop_list.setdefault(i['ingredient_name'], dict_i)
            else:
                print("нет такого блюда")
        print(shop_list)
        return

cook_book = CookBook()
cook_book.cook_book_read("recipes.txt")
cook_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
