cook_book = {} # пустой словарь
ingridients_dict = {'ingridient_name': None, 'quantity': None, 'measure': None} #пустой словарь с ключами
with open('meny.txt', encoding='UTF8') as dishes_list: # Добавляем название блюда в словарь и читаем ингридиенты
 for line in dishes_list:
        dish_name = dishes_list.readline()# присваиваем переменной значение строки из списка
        cook_book['dish_name'] = [] #Пока нет ингридиентов - пустой список
        ingridients_stokes = int(dishes_list.readline()) #читаем число
        ingridients_list = []#создаем список

	for ingridients in range(ingridients_stokes): # Читаем строки
		n = 0
		n += 1

		if n != int(ingridients_stokes):
			ingridients = dishes_list.readline()[:-1]
			ingridients_list.append(ingridients.split(' | ', 2)) #	Разбиение строки по разделителю

    i = 1

    while i <= ingridients_stokes:
	    i += 1
	  for ingridient_name, quantity, measure in ingridients_list:
		ingridients_dict['ingridient_name'] = ingridient_name
		ingridients_dict['quantity'] = quantity
		ingridients_dict['measure'] = measure

cook_book['ingridients'] = ingridients_dict

print(cook_book)


# cook_book = {
#     'Яичница': [
#         {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#         {'ingridient_name': 'помидоры', 'quantity': 2, 'measure': 'гр.'}],
#     'Стейк': [
#         {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#         {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#     'Салат': [
#         {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#         {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'щт.'}]
# }

#dishes = ['Яичница', 'Стейк', 'Салат']
#person_count = int(input('Введите кол-во человек: '))


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    # for shop_list_item in shop_list.values():
    #   print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()