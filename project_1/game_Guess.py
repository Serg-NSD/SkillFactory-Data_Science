"""Игра 'Угадай число'.

Компьютер загадывает число и затем угадывает его менее,  
чем за 20 попыток.

"""

import numpy as np

number = np.random.randint(1, 101)    # Компьютер загадывает число от 1 до 100  
print("Hidden the number: ", number)


def game_score(number: int = 1) -> int:
    """

    Args:
        number (int, optional): Hidden the number. Defaults to 1.

    Returns:
        int: Average count of attempts.
    """
    
    count = 0    # Счётчик попыток
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
    
    return count


game_score(number)