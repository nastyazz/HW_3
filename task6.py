n = int(input())
a = []
for i in range(n): #запрос n
    row = input().split(' ') #каждая строка разделяется на элементы
    if len(row) == n:
        a.append(row) #если кол-во элементов равно n, то строка добавляется в список a
    else:
        print("Неверное кол-во чисел в строке")


def is_symmetric(a):
    for i in range(len(a)): #проверка с помощью вложенного цикла для проверки, является ли список а симметричным
        if len(a) == len(a[i]): #относительно главной диагонали
            for j in range(len(a)):
                if a[i][j] != a[j][i]:
                    return 'no'
        else:
            return 'no' #иначе нет
    return 'yes'  #если да, то возвращаем yes
print(is_symmetric(a))