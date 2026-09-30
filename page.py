balance = 70.00
print("Ваш баланс:", balance)

steam_games = [("Asseto Corsa", 10.0), ("Forza Horizon 5", 30.0), ("eFootball 2025", 0.0),
               ("Grand Theft Auto", 12.99), ("Cyberpunk 2077", 45.0),
               ("Warframe", 0.0), ("FC 25", 69.99)]

biblioteka = []

while True:
    print("1. Магазин")
    print("2. Библиотека")
    print("3. Добавить игру в библиотеку")
    print("4. Удалить игру из библиотеки")
    print("5. Посмотреть баланс")
    print("6. Выйти из стима")
    choose = input()

    if choose == "1":
        print("Магазин")
        for games, price in steam_games:
            if price == 0.0:
                price_info = "Бесплатно"
            else:
                price_info =  price
            print(games, price_info)

    elif choose == "2":
        print("Библиотека")
        if biblioteka:
            for games in biblioteka:
                print(games)
        else:
            print("В вашей библиотеке нет игр")

    elif choose == "3":
        games = input("Введите название игры: ")
        games_found = False
        for game, price in steam_games:
            if games == game:
                games_found = True
                if price == 0.0:
                    biblioteka.append(games)
                    print("Игра успешно добавилась в вашу библиотеку")
                elif balance >= price:
                    biblioteka.append(games)
                    balance -= price
                    print("Игра куплена и успешно добавлена в вашу библиотеку", games)
                else:
                    print("Недостаточно средств на балансе")
                break
        if not games_found:
            print("Игра не найдена в магазине")

    elif choose == "4":
        games = input("Введите название игры: ")
        if games in biblioteka:
            biblioteka.remove(games)
            print("Игра удалена из вашей библиотеки:", games)
        else:
            print("Такой игры нет в вашей библиотеке")

    elif choose == "5":
        print("Ваш баланс:", balance)

    elif choose == "6":
        print("Вы вышли из стима")
        break