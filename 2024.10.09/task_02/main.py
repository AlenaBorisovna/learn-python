def split_test_str(s: str, separator: list[str]) -> list[str]:
    result: list[str] = ['']

    for symbol in text:
        splits = s.split(symbol)
        waiting_for_sep = [splits for splits in splits if splits.split()]
        result.extend(waiting_for_sep)

    return result


if __name__ == '__main__':
    seps: list[str] = [';', '.', ',', '!', '?']

    test_str = " Строка1; Строка2. Строка3."
    print(split_test_str(test_str, seps))
