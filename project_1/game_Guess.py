"""Игра 'Угадай число'.
Компьютер загадывает число и затем угадывает его менее, чем за 20 попыток.

"""

import numpy as np

number = np.random.randint(1, 101)    # Компьютер загадывает число от 1 до 100  
print("\nЗагаданное число: ", number)


def game_score(number: int = 1) -> int:
    """

    Args:
        number (int, optional): Hidden the number. Defaults to 1.

    Returns:
        int: Count of attempts.
    """
    
    count = 0    # Счётчик попыток  
    min_number = 1    # Нижняя граница поиска  
    max_number = 101    # Верхняя граница поиска  
    
    while True:
        count += 1
        random_array = np.random.randint(min_number, max_number, size=(1000))  # Загадали список чисел с учётом границ  
        predict_number = (min_number + max_number) // 2
        print(f'Попытка №: {count}   Число {predict_number}')
        if number > predict_number:
            min_number = predict_number    # Переназначение нижней границы поиска  
            
        elif number < predict_number:
            max_number = predict_number    # Переназначение верхней границы поиска  
            
        else:
            print(f'Количество попыток: {count}\n')
            break
    
    return count


game_score(number)