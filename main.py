import datetime
import os
from Password import Password
from rich import print, box
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console, Group
from rich.text import Text
from rich.table import Table


def file_name():
    text_datetime = f'{datetime.datetime.now()}'
    symbol_replace = ['.', ':', '-', ' ']
    fn = ''
    for s in text_datetime:
        is_write = True
        for sr in symbol_replace:
            if s == sr:
                fn += '_'
                is_write = False
        if is_write:
            fn += s
    return fn


password = Password()

count_symbols = input("Введите количество символов в пароле: ")
pin_code = input("Введите PIN CODE для шифрования пароля (4 цифры): ")

if not pin_code.isdigit():
    pin_code = None

if count_symbols.isdigit():
    password.generation(int(count_symbols), pin_code)
else:
    password.generation(None, None)

# print(f'Приложение версии 0.0.1')
# print(f'Количество доступных символов: {len(password.get_array_symbols())}')
# print(f'Доступные символы: {password.get_array_symbols()}')
# print(f'Количество возможных комбинаций: {password.count_variant}')
#
# print(f'Сгенерированный пароль: {password.password}')

console = Console()
layout = Layout(name="info")

table_info = Table.grid(padding=1)

print_count_array_symbols = Text.from_markup(f'{len(password.get_array_symbols())}', style="bold yellow")
table_info.add_row(f'Количество доступных символов:', print_count_array_symbols)

print_array_symbols = Text.from_markup(f'{password.get_array_symbols()}', style="bold yellow")
table_info.add_row(f'Доступные символы:', print_array_symbols)

print_count_variant = Text.from_markup(f'{password.count_variant}', style="italic #af00ff")
table_info.add_row(f'Количество возможных комбинаций:', print_count_variant)

print_password = Text.from_markup(f'{password.password}', style="bold yellow")
table_info.add_row(f'Сгенерированный пароль:', print_password)

print_pin_code = Text.from_markup(f'{password.pin_code}', style="bold yellow")
table_info.add_row(f'Пин код:', print_pin_code)

print_check_summa = Text.from_markup(f'{password.check_summa}', style="bold yellow")
table_info.add_row(f'Ключ пароля:')

layout.update(
    Panel(
        Group(table_info, print_check_summa),
        box=box.ROUNDED,
        title="Информация",
        subtitle="Приложение версии 0.0.7",
    )
)

console.print(layout)

if not os.path.exists('password'):
    os.mkdir('password')

# Запись пароля в файл.
with open(f'password/{file_name()}.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password.check_summa}'))

input()
