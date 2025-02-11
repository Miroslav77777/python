
while(True):
    print('Добро пожаловать в калькулятор 👌😂 \n'
          'Список доступных операций: \n'
          '+    -    /    *    mod    pow    div \n'
          'Чтобы выйти, напишите "exit" на любом этапе')
    x = input('Введите 1-е число: ')
    if(x == 'exit'):break
    y = input('Введите 2-е число: ')
    if(y == 'exit'):break
    op = input('Введите операцию: ')
    if (op == 'exit'): break

    match op:
        case '+':
            print('Результат + ... ', float(x)+float(y))
        case '-':
            print('Результат - ... ', float(x)-float(y))
        case '/':
            if(y == 0):
                print('Деление на 0!')
            else:
                print('Результат / ... ', float(x)/float(y))
        case '*':
            print('Результат * ... ', float(x)*float(y))
        case 'mod':
            print('Результат mod ...', int(x)%int(y))
        case 'pow':
            print('Результат pow... ', pow(float(x), float(y)))
        case 'div':
            if (y == 0):
                print('Деление на 0!')
            else:
                print('Результат div ... ', int(x) // int(y))