X = int(input('Введите количество программистов: '))
end = X%10

match end:
    case '1':
        print(X , ' Программист')
    case _ if end in {'2', '3', '4'}:
        print(X , 'Программиста')
    case _:
        print(X , 'Программистов')