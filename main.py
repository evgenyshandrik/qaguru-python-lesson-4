import inspect


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__


def open_browser(browser_name):
    print_name_function(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_name_function(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_name_function(find_registration_button_on_login_page, page_url, button_text)


# print steps (old version)
def print_name_functions_v1(*args):
    print('Steps to reproduce:')
    for step, item in enumerate(args):
        print(f"{step + 1}: {item.__name__.capitalize().replace('_', ' ')} ", end='')
        params = inspect.getfullargspec(item)
        if len(params.args) != 0:
            print(params.args)
        else:
            print()


# print name function
def print_name_function(func, *args):
    print(f"{func.__name__.capitalize().replace('_', ' ')}", end=' ')
    value_args = list(func.__code__.co_varnames)
    end_symbol = ', '
    if args:
        print('(', end='')
    for i, arg in enumerate(args):
        if i == len(args) - 1:
            end_symbol = ''
        print(value_args[i].replace('_', ' '), arg, sep=': ', end=f'{end_symbol}')

    if args:
        print(')', end='')
    print()


if __name__ == '__main__':
    open_browser('Chrome')
    go_to_companyname_homepage('/home')
    find_registration_button_on_login_page('/sign_up', 'Register')
