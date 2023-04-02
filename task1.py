def can_eat(horse_coordinates, enemy_coordinates): #задаем аргументы про коордианты лошоди и врага(другой фигуры)
    difference_x = abs(horse_coordinates[0] - enemy_coordinates[0]) #разность по 1 координате
    difference_y = abs(horse_coordinates[1] - enemy_coordinates[1]) #разность по 2 координате
    return (difference_x == 2 and difference_y == 1) or (difference_x == 1 and difference_y == 2)
#х - это ход коня по вертикале, у - по горизонтале
result = can_eat((2, 1), (4, 2))
print('result =', result) #выодим правду или ложь и именновый аргумент
