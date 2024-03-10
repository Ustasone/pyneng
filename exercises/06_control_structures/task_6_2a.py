# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
broadcast = "255.255.255.255"
zero = "0.0.0.0"
ipaddress = input('Введите ip-адрес в формате 10.0.1.1: ')
mark = 1
err = 0
ipadd = ipaddress.split('.')
count = len(ipadd)
if count == 4:
    for octet in ipadd:
        if octet.isdigit():
            if int(octet) >= 0 and int(octet) <= 255:
                digit = 1
            else:
                mark = 0
                digit = 1
               
        else:
            digit = 0
            mark = 0
            break
else:
     err = 1

if count == 4 and digit == 1 and mark == 1 and err == 0:
    if int(ipadd[0])  >= 1 and int(ipadd[0]) <= 223: 
       print('unicast') 
    elif int(ipadd[0]) >= 224 and int(ipadd[0]) <= 239:
       print('multicast')
    elif broadcast == ipaddress:
       print('local broadcast')
    elif zero == ipaddress:
       print('unassigned')
    else:
        print('unused')
else:
    print('Неправильный IP-адрес')
