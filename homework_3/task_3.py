MAX_WEIGHT = 10
ITEM_TRIP = {'палатка': 5, 'еда': 4, 'вода': 3, 'топор': 2, 'аптечка': 1}


def find_combination(items: dict[str, int]) -> list[list[str, int]]:
    weight_backpack: int = 0
    backpack_configuration: list[list[str, int]] = []
    for thing, weight in items.items():
        if weight_backpack + weight <= MAX_WEIGHT:
            backpack_configuration.append([thing, weight])
            weight_backpack += weight
    return backpack_configuration


def print_contents_backpack(backpack) -> None:
    weight_backpack: int = 0
    print("Конфигурация рюкзака:")
    for item in backpack:
        print(f'{item[0]} ({item[1]}кг)')
        weight_backpack += item[1]
    print(f'Вес рюкзака: {weight_backpack}кг')


def print_contents_backpack_full(backpack) -> None:
    count = 1
    for configuration in backpack:
        weight_backpack: int = 0
        print(f"Конфигурация рюкзака №{count}:")
        for item in configuration:
            print(f'{item} ({ITEM_TRIP[item]}кг)')
            weight_backpack += ITEM_TRIP[item]
        print(f'Вес рюкзака: {weight_backpack}кг\n')
        count += 1


def find_all_combinations(items) -> list[list[str]]:
    list_things = list(items.keys())
    backpack_configuration: list[list[str]] = []
    weight_backpack: int = 0
    backpack: list[str] = []

    for item in range(len(list_things)):
        backpack_configuration.append([list_things[item]])
        value = 1
        while value+item < len(list_things):
            backpack.append(list_things[item])
            weight_backpack += items[list_things[item]]
            for thing in list_things[item+value::]:
                if weight_backpack + items[thing] <= MAX_WEIGHT:
                    backpack.append(thing)
                    weight_backpack += items[thing]
            backpack_configuration.append(backpack)
            value += 1
            weight_backpack = 0
            backpack = []
    return backpack_configuration


if __name__ == '__main__':
    print("Вывести одно значение!")
    print_contents_backpack(find_combination(ITEM_TRIP))
    print()
    print("Повышенная сложность!")
    print(print_contents_backpack_full(find_all_combinations(ITEM_TRIP)))
