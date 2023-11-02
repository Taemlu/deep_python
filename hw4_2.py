# Напишите функцию, принимающую на вход только ключевые параметры
# и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хэшируем, используйте его строковое представление
# reverse_kwargs(rev=True, acc="YES", stroka=4) ->
# {True: "rev", "YES": 'acc', 4: "stroka"}

def dict_kwargs(**kwargs) -> dict:
    kwargs_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is not None:
            kwargs_dict[value] = key
        else:
            kwargs_dict[str(value)] = key
    return kwargs_dict


print(dict_kwargs(rev=True, acc="YES", stroka=4))
