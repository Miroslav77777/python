X = input('Введите номер билета: ')

first_three = [int(dight) for dight in X[:3]]
last_three = [int(dight2) for dight2 in X[-3:]]

if(sum(first_three)==sum(last_three)):
    print('Счастливый')
else:
    print('Обычный')

