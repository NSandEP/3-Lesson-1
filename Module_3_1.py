calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [string.upper() for string in list_to_search]
a = str(input('Введите первое слово: '))
b = str(input('Введите второе слово: '))
print(string_info(a))
print(string_info(b))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
