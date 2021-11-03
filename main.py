import datetime
import os
from Password import Password
from rich import print, box
from rich.layout import Layout
from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text

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

count_symbols = input('Введите количество символов в пароле: ')


if count_symbols.isdigit():
    password.generation(int(count_symbols))
else:
    password.generation(None)


#print(f'Приложение версии 0.0.1')
#print(f'Количество доступных символов: {len(password.get_array_symbols())}')
#print(f'Доступные символы: {password.get_array_symbols()}')
#print(f'Количество возможных комбинаций: {password.count_variant}')
#
#print(f'Сгенерированный пароль: {password.password}')


console = Console()
layout = Layout(name="info")

print_count_array_symbols = Text.from_markup(
    f'Количество доступных символов: {len(password.get_array_symbols())}',
    style="bold yellow"
)

print_array_symbols = Text.from_markup(
    f'Доступные символы: {password.get_array_symbols()}',
    style="bold yellow"
)

print_count_variant = Text.from_markup(
    f'Количество возможных комбинаций: {password.count_variant}',
    style="bold yellow"
)

print_password = Text.from_markup(
    f'Сгенерированный пароль: {password.password}',
    style="bold yellow"
)

layout.update(
    Panel(
        Group(
            print_count_array_symbols,
            print_array_symbols,
            print_count_variant,
            print_password
        ),
        box=box.ROUNDED,
        title="Информация",
        subtitle="Приложение версии 0.0.1",
        style="blue",
        border_style="red",
    )
)


console.print(layout)



if not os.path.exists('password'):
    os.mkdir('password')

# Запись пароля в файл.
with open(f'password/{file_name()}.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))

input()

