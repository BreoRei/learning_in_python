WITHDRAWAL_PERCENTAGE = 0.015
MINIMUM_WITHDRAWAL = 30
MAXIMUM_WITHDRAWAL = 600
MINIMUM_AMOUNT = 50
DEPOSIT_INTEREST = 0.03
TAX_ON_WEALTH = 0.1
AMOUNT_TAXED = 5_000_000
OPERATIONS_FOR_INTEREST = 3


def get_value(request_text: str) -> int:
    while True:
        try:
            amount_money: int = int(input(request_text))
            if amount_money % MINIMUM_AMOUNT == 0:
                return amount_money
            else:
                print("Введена неверная сумма")
        except ValueError:
            print("Ошибка ввода")


def get_interest(money: int) -> float:
    if money * WITHDRAWAL_PERCENTAGE < MINIMUM_WITHDRAWAL:
        return MINIMUM_WITHDRAWAL
    elif money * WITHDRAWAL_PERCENTAGE > MAXIMUM_WITHDRAWAL:
        return MAXIMUM_WITHDRAWAL
    else:
        return money * WITHDRAWAL_PERCENTAGE


def atm_operation() -> list[tuple[str, int]]:
    cash: float = 0
    count: int = 0
    operations_history = []
    while True:
        print(f"\n{'*' * 30}\nБаланс равен {cash:.2f} y.e.\n{'*' * 30}\n")
        print(f"""1 Пополнить счет
2 Снять средства со счета
3 История операций
4 Выйти""")
        operation = input("Введите номер операции -> ")
        if cash > AMOUNT_TAXED:
            cash -= cash * TAX_ON_WEALTH
        match operation:
            case '1':
                count_percentages = get_value("Сумма пополнения кратна 50 у.е.\nВведите сумму -> ")
                cash += count_percentages
                count += 1
                operations_history.append(("Внесение", count_percentages))
            case '2':
                count_percentages = get_value("Cумма снятия кратнуа 50 у.е.\nВведите сумму -> ")
                interest: float = get_interest(money=count_percentages)
                withdrawal_amount: float = count_percentages + interest
                if cash < withdrawal_amount:
                    print("На счете недостаточно денег")
                else:
                    cash -= withdrawal_amount
                    count += 1
                    operations_history.append(("Снятие", count_percentages))
            case '3':
                print("\nИстория операций:")
                for operation, money in operations_history:
                    print(f'{operation:<8}: {money:>10} рублей')
            case '4':
                break
            case _:
                print("Неверный номер операции")
        if count == OPERATIONS_FOR_INTEREST:
            cash += cash * DEPOSIT_INTEREST
            count = 0
    return operations_history


if __name__ == '__main__':
    history = atm_operation()
    print(history)