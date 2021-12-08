"""Игра 'Угадай число'.
Компьютер загадывает число и затем угадывает его менее, чем за 20 попыток.
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем числа, соблюдая условие:
       попыток угадывания должно быть меньше 20.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    count = 0
    max_n = 101
    min_n = 1
    while True:
        count += 1
        predict_number = (min_n + max_n) // 2
        if number > predict_number:
            min_n = predict_number    # Переназначение нижней границы поиска

        elif number < predict_number:
            max_n = predict_number    # Переназначение верхней границы поиска

        else:
            print(f"Загаданное число: {number}  Угадано на {count} попытке")
            return count


def game_score(random_predict) -> int:
    """Алгоритм вычисляет среднее количество попыток угадать число за 1000 проходов

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        str: Cреднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    result = f"Среднее количество попыток угадать число за 1000 проходов: {score}"
    return result


if __name__ == "__main__":
    game_score(random_predict)
