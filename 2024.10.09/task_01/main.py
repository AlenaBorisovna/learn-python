def text_split(s: str, separator: str) -> list[str]:
    return s.split(sep=separator)


if __name__ == '__main__':
    test_string = "Тучка золотая. Небо голубое. Солнце уходит в закат."
    print(text_split(test_string, '.'))
