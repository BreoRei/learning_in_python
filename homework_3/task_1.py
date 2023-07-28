def search_for_duplicate_values(inner_nums) -> None:
    result_list: list[int | str] = []
    for num in inner_nums:
        count: int = inner_nums.count(num)
        if count > 1 and num not in result_list:
            result_list.append(num)
    print(result_list)


if __name__ == '__main__':
    search_for_duplicate_values(inner_nums=[1, 2, 3, "q", 1, 2, "a", 4, 1, 6, 5, "q"])
