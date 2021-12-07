"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

   # while True:

    #count = 0    # Счётчик попыток
    min_number = 1
    max_number = 101

    while count < 21:
        count += 1
        random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
        predict_number = (min_number + max_number) // 2

        if number > predict_number:
            min_number = predict_number    # Переназначение нижней границы поиска

        elif number < predict_number:
            max_number = predict_number    # Переназначение верхней границы поиска

        else:
            print(f'Average count of attempts: {count}.')
            break

        '''
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        '''

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


score_game(random_predict)

# if __name__ == '__main__':
# RUN
#    score_game(random_predict)
