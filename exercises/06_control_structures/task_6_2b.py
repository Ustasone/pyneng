# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
broadcast = "255.255.255.255"
zero = "0.0.0.0"
dig_in_ipadd = 0

while dig_in_ipadd != 4:
    ipaddress = input('Введите ip-адрес в формате 10.0.1.1: ')
    ipadd = ipaddress.split('.')
    octet_count = len(ipadd)
    if octet_count == 4:
        for octet in ipadd:
            if octet.isdigit():
                if int(octet) >= 0 and int(octet) <= 255:
                    dig_in_ipadd = dig_in_ipadd + 1
                else:
                    dig_in_ipadd = 0
                    print('Неправильный IP-адрес')
                    break
            else:
                dig_in_ipadd = 0
                print('Неправильный IP-адрес')
                break
    else:
        print('Неправильный IP-адрес')

if dig_in_ipadd == 4 :
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
    pass

