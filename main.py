def initial_field() -> list[list[str]]:
    """
    Создаёт исходное игровое поле для игры в крестики нолики. Размер поля может варьироваться от 3 до 6.
    :return: двухмерный массив с размером size x size
    """
    print("Введите размер поля, целое число от 3 до 6")
    while True:
        size = input()
        if size.isdigit():
            if 3 <= int(size) <= 6:
                return [[" " for _ in range(int(size))] for _ in range(int(size))]
        else:
            print("Размер поля должен быть целое число от 3 до 6")


def draw_field(field: list[list[str]]) -> None:
    """
    Функция рисует игровое поле
    :param field: исходное поле
    :return: None
    """
    for row in field:
        for cell in row:
            print(f"|{cell}", end="")
        print("|")


def player_change(field: list[list[str]]) -> list[str]:
    """
    Выдаёт последовательность ходов игроков, в зависимости от размера поля и кто ходит первый
    :param field: начальное игровое поле
    :return: список последовательности ходов
    """
    print("Кто будет ходить первым? Введите X или O")
    players = []
    while True:
        player = input()
        if player in ["X", "x", "х", "Х", "ч", "Ч", "[", "{"]:
            for i in range(len(field) ** 2):
                players.append("X") if i % 2 == 0 else players.append("O")
            return players
        elif player in ["O", "o", "0", "О", "о", "J", "j", "щ", "Щ"]:
            for i in range(len(field) ** 2):
                players.append("X") if i % 2 == 1 else players.append("O")
            return players
        else:
            print("Введите игрока правильно: X или O")


def move(field: list[list[str]], player: str):
    """
    Принимает на вход игровое поле в виде двумерного массива и заменяет одно значение
    :param field: Игровое поле в виде двумерного массива
    :param player: Игрок, чей ход на данный момент
    :return: измененное игровое поле
    """
    len_ = len(field)
    print(f"Ходит игрок {player}\nКуда хотите сделать ход?")
    while True:
        row = input(f"Ведите номер строки от 1 до {len_}\n")
        if row.isdigit() and (1 <= int(row) <= len_):
            sell = input(f"Ведите номер столбца от 1 до {len_}\n")
            if sell.isdigit() and (1 <= int(sell) <= len_):
                if field[int(row) - 1][int(sell) - 1] == " ":
                    field[int(row) - 1][int(sell) - 1] = player
                    break
                else:
                    print("Ячейка занята, введите адрес пустой ячейки")
            else:
                print(f"Столбцы нумеруются от 1 до {len_}")
        else:
            print(f"Строки нумеруются от 1 до {len_}")


def somebody_won(field: list[list[str]]) -> str:
    """
    Проверяет, выиграл кто-то или нет. Если выиграл, выводит кто.
    :param field: Игровое поле в виде двумерного массива
    :return: Кто выиграл, может принимать значения X, O, -
    """
    len_ = len(field)
    for row in range(len_):  # Проверка по строке
        if field[row][0] != " " and all([field[row][0] == cell for cell in field[row][1:]]):
            return field[row][0]
    for column in range(len(field[0])):  # Проверка по колонке
        if field[0][column] != " " and all([field[0][column] == cell for cell in [x[column] for x in field][1:]]):
            return field[0][column]
    if field[0][0] != " " and all([field[0][0] == field[i][i] for i in range(1, len_)]):
        return field[0][0]  # Проверка по диагонали сверху вниз
    if field[len_ - 1][0] != " " and all([field[len_ - 1][0] == field[len_ - 1 - i][i] for i in range(1, len_)]):
        return field[len_ - 1][0]  # Проверка по диагонали снизу вверх
    return "-"


def game_tic_tac_toe():
    playing_field = initial_field()  # Создаём пустое поле с элементами " "
    list_players = player_change(playing_field)  # Создаём список ходов игроков по очереди
    draw_field(playing_field)  # Печатаем в консоль пустое поле
    for i in list_players:  # Пробегаем по порядку ходов игроков
        move(playing_field, i)  # Вызываем функцию, которая ставит ход игрока
        draw_field(playing_field)  # После каждого хода печатаем поле заново
        win = somebody_won(playing_field)  # Проверяем выиграл ли кто то
        if win == "X":
            print("Победил игрок X")
            break
        elif win == "O":
            print("Победил игрок O")
            break
    else:  # Если никто не выиграл и цикл дошёл до конца, значит все ячейки заполнены и никто не выиграл
        print("Ничья")


if __name__ == '__main__':
    game_tic_tac_toe()
