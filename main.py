import re
from collections import Counter


def filter_5letter_words():
    """
    Filter russian nouns and create new file with 5 letters words only
    """
    with open("russian_nouns.txt", encoding="utf-8") as rn, open(
        "n5.txt", "w", encoding="utf-8", newline="\n"
    ) as n5:
        for word in rn.readlines():
            if len(word.strip()) == 5:
                n5.write(word.strip())


def get_char_rating():
    """
    Make char rating from 5 letters words to define good start tactic
    """
    rating = Counter()
    with open("n5.txt", encoding="utf-8") as n5:
        for word in n5.readlines():
            rating.update(Counter(set(word.strip())))
    return rating


def solver(exclude: str = "", include: str = "", pattern: str = ".....") -> list:
    """
    Find words matching patterns
    :param exclude: Chars that ARE NOT in target word
    :param include: Chars that ARE in target word
    :param pattern: Pattern for chars in correct position, if any
    :return:
    """
    result = []
    with open("n5.txt", encoding="utf-8") as n5:
        for word in n5.readlines():
            word = word.strip()
            if (
                all((char not in word for char in exclude))
                and all((char in word for char in include))
                and re.fullmatch(pattern, word)
            ):
                result.append(word)
    return result

exclude_ = input("Ввод отсутствуюших букв:")
include_ = input("Ввод присутствующих букв:")
pattern_ = input("Ввод паттерна:")
if __name__ == '__main__':
    candidates = solver(exclude=exclude_, include=include_, pattern=pattern_)
    print(len(candidates))
    print(*candidates, sep=" ")
