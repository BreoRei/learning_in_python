HEX_NUMBER = 16


def get_hex_number() -> None:
    hex_string: str = ''
    hexadecimal_digits: dict[int:str] = {0: '0', 1: '1', 2: '2', 3: '3',
                          4: '4', 5: '5', 6: '6', 7: '7',
                          8: '8', 9: '9', 10: 'A', 11: 'B',
                          12: 'C', 13: 'D', 14: 'E', 15: 'F',
                          }
    hex_num: int = get_value()
    hex_iter: int = hex_num
    while hex_iter > 0:
        hex_string = hexadecimal_digits[hex_iter % HEX_NUMBER] + hex_string
        hex_iter //= HEX_NUMBER
    print(f'Число {hex_num} в 16-ой представлении: {hex_string}\n'
          f'Проверка с помощью функции hex: {hex(hex_num)}')


def get_value() -> int:
    while True:
        try:
            return int(input("Введите число для перевода в 16-ую систему -> "))
        except ValueError:
            print("Ошибка. Это не число.")


if __name__ == '__main__':
    get_hex_number()
