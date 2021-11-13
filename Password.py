import random
import hashlib


class Password:
    # Набор доступных символов.
    ARRAY_SYMBOLS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z',
                     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z',
                     '!', '@', '#', '$', '&', '?', '-', '+', '=', '~',
                     '_', '^', '*', '.']

    # Получаем количество символов в пароле.
    COUNT_SYMBOLS = 4

    def __init__(self):
        self.password = None
        self.count_symbols = self.COUNT_SYMBOLS
        self.count_variant = 0
        self.check_summa = ''
        self.pin_code = ''

    def generation(self, count_symbols=None, pin_code=None):
        if count_symbols is not None:
            self.count_symbols = count_symbols
        if pin_code is not None:
            self.pin_code = pin_code

        # Узнаем количество всех возможных комбинаций.
        self.count_variant = len(self.ARRAY_SYMBOLS) ** self.count_symbols

        # Генерируем уникальный пароль.
        password = ''
        for i in range(0, self.count_symbols):
            password = password + f'{self.random_symbols()}'

        self.password = password
        self.check_summa = hashlib.sha512(f'{password}{self.pin_code}'.encode()).hexdigest()

    # Получить случайный символ.
    def random_symbols(self):
        return self.ARRAY_SYMBOLS[
            random.randint(0, len(self.ARRAY_SYMBOLS) - 1)
        ]

    def get_symbol(self, number):
        return self.ARRAY_SYMBOLS[number]

    def get_array_symbols(self):
        return self.ARRAY_SYMBOLS
