import numpy as np

count = 0
#number = 82
number = np.random.randint(1, 101)    # Компьютер загадывает число от 1 до 100  
print(number)

#while True:
    #count += 1
    #predict_number = np.random.randint(1, 101)  # предполагаемое число
    #if number == predict_number:
        #break  # выход из цикла если угадали
    
min_number = 1
max_number = 101


while True:
    count += 1
    random_array = np.random.randint(min_number, max_number, size=(1000))  # загадали список чисел
    predict_number = (min_number + max_number) // 2
    print(min_number, ' ', max_number, ' ', predict_number)
    if number > predict_number:
        min_number = predict_number    # Переназначение нижней границы поиска

    elif number < predict_number:
        max_number = predict_number    # Переназначение верхней границы поиска

    else:
        print(f'Average count of attempts: {count}.')
        break
    

