"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

number = np.random.randint(1, 100)  # компьютер загадывает число от 1 до 100
print('Hidden the number: ', number)


def game_score(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0   # счетчик попыток
    min_number = 1  # нижняя граница поиска числа
    max_number = 101  # верхняя граница поиска числа

    while count < 21:
        count += 1
        predict_number = (min_number + max_number) // 2

        if number > predict_number:
            min_number = predict_number  # смещение нижней границы поиска числа

        elif number < predict_number:
            max_number = predict_number  # смещение верхней границы поиска числа

        else:
            print(f'Average count of attempts: {count}.')
            break
    return count


game_score(number)


# if __name__ == '__main__':
#    #RUN
#    score_game(random_predict)
