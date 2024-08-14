import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        current_datetime = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(f'Function: {old_function.__name__}\n'
                    f'Date: {current_datetime}\n'
                    f'Params: {args}, {kwargs}\n'
                    f'Result: {result}\n'
                    f'\n')
        return result

    return new_function
