import inspect


def open_browser(browser, version):
    pass


def go_to_companyname_homepage(url):
    pass


def find_registration_button_on_login_page():
    pass


# Print steps
def print_name_functions(*args):
    print('Steps to reproduce:')
    for step, item in enumerate(args):
        print(f"{step + 1}: {item.__name__.capitalize().replace('_', ' ')} ", end='')
        params = inspect.getfullargspec(item)
        if len(params.args) is not 0:
            print(params.args)
        else:
            print()


if __name__ == '__main__':
    print_name_functions(open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)
