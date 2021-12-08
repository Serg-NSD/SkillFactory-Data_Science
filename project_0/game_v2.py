"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

''' Lekov
def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        
        
    return count
'''

def random_predict(number: int = 1) -> int:
    count = 0
    max_n = 101
    min_n = 1
    print('число: ', number)
    while True:
        count += 1
        predict_number = (min_n + max_n) // 2
        if number > predict_number:
            min_n = predict_number    # Переназначение нижней границы поиска

        elif number < predict_number:
            max_n = predict_number    # Переназначение верхней границы поиска

        else:
            return count
           # score = int(np.mean(count_ls))
           # itog = "\nЗагаданное число: " + str(number) + "\nКоличество попыток: " +\
           # str(count) + "\nСреднее количество попыток: " + str(score)
           # break
        

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    count_dt ={}
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    #print(random_array)
    for number in random_array:
        count_ls.append(random_predict(number))
        count_dt.update({number: "количество попыток " + str(random_predict(number))})
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток. {count_ls}")
    #print(count_dt)
    return score

score_game(random_predict)

#if __name__ == "__main__":
    # RUN
#    score_game(random_predict)
    
    
