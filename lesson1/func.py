""" def get_summ(one, two, delimiter='&'):
    first_str = str(one)
    second_str = str(two)
    user_delimiter = str(delimiter)
    result_str = first_str + delimiter + second_str
    return result_str.upper()

func_result = get_summ("Learn", "python")
print(func_result)
print(get_summ("Learn","python","|")) """


def format_price (price):
    price = int(price)
    return str(f"Цена {price} руб.")

print(format_price(56.24))