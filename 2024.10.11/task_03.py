SEPARATORS = set('.;!?')


def join_similar_segments(segment: list[str], seps: set[str]) -> list[str]:
    if not segment:
        return []

    result: list[str] = ['']
    for segments in segment:
        result[-1] += segments
        if segments.strip()[-1] in seps and segments is not segment[-1]:
            result.append('')

    return result


if __name__ == "__main__":
    text: list[str] = ['Вышел корень', ' из т', 'умана; ', 'Вынул но', 'жик из кармана. ', 'Раз, два, всё?..']

    print(join_similar_segments(text, SEPARATORS))
