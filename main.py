#Чтоб постоянно не перезапускать программу тому безумцу кто это запустил
while(True):

    #Три стороны триугольника!!
    firstAngle = float(input('Первый угол: '))
    secondAngle = float(input('Второй угол: '))
    thirdAngle = float(input('Третий угол: '))

    # Считаем периметр, на глаз измеряем площадь
    perimeter = (firstAngle + secondAngle + thirdAngle) / 2
    areaT = (perimeter*(perimeter-firstAngle)*(perimeter-secondAngle)*(perimeter-thirdAngle)) ** 0.5

    #Выводим площадь
    print('Площадь штуки с 3мя сторонами = %0.2f' %areaT)

    #Спрашиваем хочет ли пользователь(тот самый безумец) продолжить узнавать площадь той штуки
    loop = input('Продолжаем? y/n  ')
    if(loop == 'y'):
        continue
    elif(loop == 'n'):
        exit()