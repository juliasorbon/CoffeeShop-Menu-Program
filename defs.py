from CoffeeShopMenu import *

coffemenu = ('images\\c5d3533af5a86bd4966d9206c4ddaaee.gif', 'images\\da318526245381.563536837107b.gif',
             'images\\b8a2d007e93b475b92aea523f75feb92.gif')
cmakolikmenu = ('images\\1115353179b2a4213ea888579cf50635.gif', 'images\\original.gif', 'images\\croisant.gif')

inventoryPath = os.path.join('data', 'Menu.json')
koshel = os.path.join('data', 'KoselAll.json')
clientsPath = os.path.join('data', 'clients_baza.json')
Personal = os.path.join('data', 'Personal.json')
with open(inventoryPath, "r", encoding='utf-8') as menu:
    base_menu = json.load(menu)


def Cleaning_basket():
    with open(koshel, "r", encoding='utf-8') as menu:
        data = json.load(menu)
    data.clear()
    with open(koshel, "w", encoding='utf-8') as menu:
        json.dump(data, menu, ensure_ascii=False)

    return 'Done'


def Counting(choice):
    while True:
        amounts = enterbox(f'Скільки {choise} вам потрібно?')
        price = base_menu.get(choice).get(choise).get("Ціна")
        if base_menu.get(choice).get(choise).get("Кількість") >= int(amounts):
            koshel1 = buttonbox(f"Ви додали до кошика {amounts} {choise}", "CoffeeShop", ["Далі"],
                                image='images\\Cjey.gif')
            with open(koshel, "r", encoding='utf-8') as menu:
                data1 = json.load(menu)
            if choise in data1:
                data1[choise]["Кількість"] = data1[choise]["Кількість"] + int(amounts)
                data1[choise]["Ціна"] = data1[choise]["Кількість"] * price
            else:
                data1[choise] = {"Кількість": int(amounts), "Ціна": price * int(amounts),
                                 "Валюта": base_menu.get(choice).get(choise).get("Валюта")}
            with open(koshel, "w", encoding='utf-8') as menu:
                json.dump(data1, menu, ensure_ascii=False)
            return koshel1

        else:
            koshel2 = buttonbox(f"На жаль {choise}у такій кількості немає, введіть меншу", "CoffeeShop",
                                ["Меню", "Оплата"], image='images\\giphy.gif')


def Сhoice_of_milk(choice):
    milk = buttonbox(f"З якого молока вам приготувати {choice}", 'Milk',
                     ['Кокосове', 'Бананове', 'Вівсяне', 'Мигдальне'], image='images\\37.gif')
    if milk == 'Кокосове':
        msgbox(f'Ви вибрали {choice} на Кокосовому молоці')
    elif milk == 'Бананове':
        msgbox(f'Ви вибрали {choice} на Банановому молоці', image='images\\34.gif')
    elif milk == 'Вівсяне':
        msgbox(f'Ви вибрали {choice} на Вівсяному молоці', image='images\\36.gif')
    elif milk == 'Мигдальне':
        msgbox(f'Ви вибрали {choice} на Мигдальному молоці', image='images\\35.gif')

    return 'Done'


def Discount():
    key = 0
    choice2 = buttonbox('Чи є у вас карта на знижку?', 'CoffeShop',
                        ['Бажаєте зареєструвати', 'Я маю знижку', 'Перейти до оплати'],
                        image='images\\signing-icon-anim.gif')
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
                discount = file2.get(clients_code).get("Сума") / 500
                if discount > 20:
                    discount = 20

                name = file2.get(clients_code).get("Ім`я")
                msgbox(f'{name}, знижка {discount}%')
    elif choice2 == 'Перейти до оплати':
        pass

    return 'Done'


def Receipt():
    while True:
        with open(koshel, 'r', encoding='utf8') as file1:
            pay_r = json.load(file1)
            summ_tovar = 0.0
            info_chek = ''
            for txt in pay_r:
                info_chek += f'{txt} - {pay_r.get(txt).get("Ціна")} {pay_r.get(txt).get("Валюта")}\n'
                summ_tovar += pay_r.get(txt).get("Ціна")
            with open(clientsPath, 'r', encoding='utf8') as file1:
                pay_r = json.load(file1)
            if clients_code not in pay_r:
                msgbox(
                    f'{info_chek} \n Загальна сума покупки = {summ_tovar} \n Ваша знижка: 0%',
                    'CoffeeShop', 'Оплата', image='images\\money.gif')
            else:
                summ_zn = summ_tovar - (summ_tovar * (discount / 100))
                msgbox(
                    f'{info_chek} \n Загальна сума покупки = {summ_tovar} \n Ваша знижка:{discount}% \n Сума до оплати з урахування знижки - {summ_zn}',
                    'CoffeeShop', 'Оплата', image='images\\money.gif')


def Payment():
    pay = "Ok"
    if pay == "Ok":
        if clients_code in pay_r:
            pay_r[clients_code]['Сума'] = pay_r[clients_code]['Сума'] + summ_tovar
            with open(clientsPath, 'w', encoding='utf8') as file1:
                json.dump(pay_r, file1)
        msgbox("Оплата пройшла успішно, Приємного", image='images\\Cjey.gif')
        del_cosh = {}
        with open(koshel, 'w', encoding='utf8') as file1:
            json.dump(del_cosh, file1)
    else:
        time.sleep(5)
        del_cosh = {}
        with open(koshel, 'w', encoding='utf8') as file1:
            json.dump(del_cosh, file1)

        msgbox("Термін очікування вичерпано, вас поставлено на лічильник, наші люди йдуть до вас ,АТБ")