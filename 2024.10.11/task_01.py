def join_text_by_separators(segment: list[str], seps: list[str]) -> list[str]:
    if not segment:
        return []

    result: list[str] = ['']
    for segments in segment:
        result[-1] += segments
        if segments[-1] in seps and segments is not segment[-1]:
            result.append('')

    return result


if __name__ == "__main__":
    separators: list[str] = ['.', ',', '!', '?']
    text: list[str] = ['Дем', 'онстра', 'ция!']

    print(join_text_by_separators(text, separators))