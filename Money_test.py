import os.path
import random

from easygui import *
import json

inventoryPath = os.path.join('data', 'Menu.json')
koshel = os.path.join('data', 'KoselAll.json')
clientsPath = os.path.join('data', 'clients_baza.json')
Personal = os.path.join('data', 'Personal.json')
with open(inventoryPath, "r", encoding='utf-8') as menu:
    base_menu = json.load(menu)


class Product:
        def __init__(self):
            list_product = multenterbox("Введіть параметри продукту", "Product", ["Тип", "Назва", "Ціна", "Валюта", "Кількість"])
            self.type_prod = list_product[0]
            self.name = list_product[1]
            self.price = float(list_product[2])
            self.currency = list_product[3]
            self.count_prod = int(list_product[4])
            with open(inventoryPath, "r", encoding='utf-8') as menu:
                data = json.load(menu)
            if self.type_prod in data:
                data[self.type_prod].update({self.name: {"Назва": self.name, "Ціна": self.price, "Валюта": self.currency, "Кількість": self.count_prod}})
            else:
                data[self.type_prod] = {self.name: {"Назва": self.name, "Ціна": self.price, "Валюта": self.currency, "Кількість": self.count_prod}}
            with open(inventoryPath, "w", encoding='utf-8') as menu:
                json.dump(data, menu, ensure_ascii=False)

        def __repr__(self):
            return f'{self.type_prod}, {self.name}, ціна: {self.price} {self.currency}, кількість на складі: {self.count_prod}'

        # def salle(self, minus_cent, product):
        #     if self.money >= int(float(minus_cent) * 100):
        #         self.money -= int(float(minus_cent) * 100)
        #         self.money += product.discount()
        #     else:
        #         return f'Грошей не достатньо'



def count_tovar():
    while True:
        amounts = enterbox(f'Скільки {choise} вам потрібно?')
        price = base_menu.get(choice).get(choise).get("Ціна")
        if base_menu.get(choice).get(choise).get("Кількість") >= int(amounts):
            koshel1 = buttonbox(f"Ви додали до кошика {amounts} {choise}", "CoffeeShop", ["Меню"],image='images\\Cjey.gif')
            with open(koshel, "r", encoding='utf-8') as menu:
               data1 = json.load(menu)
            if choise in data1:
                data1[choise]["Кількість"] = data1[choise]["Кількість"] + int(amounts)
                data1[choise]["Ціна"] = data1[choise]["Кількість"] * price
            else:
                data1[choise] = {"Кількість": int(amounts), "Ціна": price * int(amounts), "Валюта": base_menu.get(choice).get(choise).get("Валюта")}
            with open(koshel, "w", encoding='utf-8') as menu:
                json.dump(data1, menu, ensure_ascii=False)
            return koshel1

        else:
            koshel2 = buttonbox(f"На жаль {choise}у такій кількості немає, введіть меншу", "CoffeeShop", ["Меню", "Оплата"],image='images\\giphy.gif')

def clear_koshel():
    with open(koshel, "r", encoding='utf-8') as menu:
        data = json.load(menu)
    data.clear()
    with open(koshel, "w", encoding='utf-8') as menu:
        json.dump(data, menu, ensure_ascii=False)



coffemenu = ('images\\c5d3533af5a86bd4966d9206c4ddaaee.gif','images\\da318526245381.563536837107b.gif','images\\b8a2d007e93b475b92aea523f75feb92.gif')
cmakolikmenu =('images\\1115353179b2a4213ea888579cf50635.gif','images\\original.gif','images\\croisant.gif')


while True:
    choice = buttonbox("Ласкаво просимо в кав'ярню", 'CoffeeShop', ['Перейти до покупки', "Персонал", 'Вихід'],image='images\\212409.gif')
    if choice == 'Перейти до покупки':
        with open(inventoryPath, "r", encoding='utf-8') as menu:
            base_menu = json.load(menu)
        while True:
            choice = buttonbox("Що бажаєте купити?: ", "CoffeeShop", ['Кава', "Смаколики", "Оплата", "Відміна"],image='images\\763a73bb9b8e0bdf01e02f523946a313.gif')
            if choice == "Кава":
                but = []
                [but.append(i) for i in base_menu[choice].keys()]
                but.append("Відміна")
                lst = ""
                for txt in base_menu.get(choice):
                    lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
                choise = buttonbox(lst, "CoffeeShop", but,coffemenu)
                if choise != "Відміна":
                    count_tovar()
                else:
                    continue
            elif choice == "Смаколики":
                but = []
                [but.append(i) for i in base_menu[choice].keys()]
                but.append("Відміна")
                lst = ""
                for txt in base_menu.get(choice):
                    lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
                choise = buttonbox(lst, "CoffeeShop", but,cmakolikmenu)
                if choise != "Відміна":
                    count_tovar()
                else:
                    continue
            elif choice == 'Оплата':
                key = 0
                choice2 = buttonbox('Чи є у вас карта на знижку?', 'CoffeShop',
                                    ['Бажаєте зареєструвати', 'Я маю знижку', 'Перейти до оплати'],image='images\\signing-icon-anim.gif')
                if choice2 == 'Бажаєте зареєструвати':
                    with open(clientsPath, 'r', encoding='utf-8') as file1:
                        file2 = json.load(file1)
                    key = random.randrange(1000000, 9999999)
                    name = enterbox("Введіть ваше ім`я")
                    msgbox(f'{name} Ваш код для знижки - {key}')
                    file2[key] = {'Ім`я': name, 'Знижка': 0, 'Сума': 0}
                    with open(clientsPath, 'w', encoding='utf-8') as file3:
                        json.dump(file2, file3, ensure_ascii=False)
                elif choice2 == 'Я маю знижку':
                    clients_code = enterbox('Введіть свій код на знижку')
                    with open(clientsPath, 'r', encoding='utf-8') as file1:
                        file2 = json.load(file1)
                        if str(clients_code) in file2:
                            key = file2.get(clients_code).get("Code")
                            name = file2.get(clients_code).get("Ім`я")
                            msgbox(f'{name} {key}')
                elif choice2 == 'Перейти до оплати':
                    pass

                while True:
                    with open(koshel, 'r', encoding='utf8') as file1:
                        pay_r = json.load(file1)
                        summ_tovar = 0.0
                        info_chek = ''
                        for txt in pay_r:
                            info_chek += f'{txt} - {pay_r.get(txt).get("Ціна")} {pay_r.get(txt).get("Валюта")}\n'
                            summ_tovar += pay_r.get(txt).get("Ціна")
                        if key == 0:
                            msgbox(
                                f'{info_chek} \n Загальна сума покупки = {summ_tovar} \n Ваша знижка:{key}',
                                'CoffeeShop', 'Оплата',image='images\\money.gif')
                        else:
                            msgbox(
                            f'{info_chek} \n Загальна сума покупки = {summ_tovar} \n Ваша знижка:{file2[key].get("Знижка")}',
                            'CoffeeShop', 'Оплата',image='images\\money.gif')
                            # msgbox(f"{pay_r[key].get('Знижка')} , {type(pay_r[key].get('Знижка'))}")

            elif choice == 'Відміна':
                clear_koshel()
                break

    elif choice == "Персонал":
        choice_login = multenterbox("Введіть лигін та пароль", "CoffeeShop", ["Логін", "Пароль"])
        with open(Personal, "r", encoding='utf-8') as menu:
            data = json.load(menu)
        if choice_login[0] == data.get(choice_login[0])["Login"]:
            if int(choice_login[1]) == data.get(choice_login[0])["Password"]:
                choice = buttonbox(f"Вхід дозволено \nНаступні дії?", "CoffeeShop", ['Додати товар', "Відмінa"],image='images\\smartparcel-empty-box.gif')
                if choice == 'Додати товар':
                    coffee1 = Product()
                else:
                    choice = "Персонал"
            else:
                msgbox("Не вірно введений пароль",image='images\\giphy.gif')
        else:
            msgbox("Такого користувача не знайдено",image='images\\giphy.gif')


    elif choice == 'Вихід':
        break

    else:
        continue