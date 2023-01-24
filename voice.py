# import speech_recognition, time,  pyautogui
# sr = speech_recognition.Recognizer()
# sr.pause_threshold = 0.5

# def listen():
#     with speech_recognition.Microphone() as mic:
#         sr.adjust_for_ambient_noise(source=mic, duration=1)
#         audion = sr.listen(source=mic)
#         voice = sr.recognize_google(audion, language='en-US').lower()
#     return voice

# with pyautogui.hold('win'):
#     pyautogui.press('shift')
# pyautogui.write('telegram', 0.15)
# pyautogui.press('enter')



# numbers = ['1', '2', '2', '4', '5', '1', '4', '18']
# counts = {}
# for number in numbers:
#     if number in counts:
#         counts[number] = +1
#     else:
#         counts[number] = 1
# for number, count in counts.items():
#     if count == 1:
#         print(number)

# x = 45
# c = x * 0.9
# per = 6.75
# while x != 0 and x <= 0:
#     x = x - per


# print(per)
# num = int(input('Input Number: '))
# while num >= 1:
#     s = num*0.9
#     num = s
#     print(num)

# r = int(input('Enter number of rows: '))
# def F_Triangle():
#     number = 1
#     for i in range(1, r+1):
#         for j in range(1, i+1):
#             if number < 10:
#                 print(f'{number}', end='  ')
#                 number = number + 1
#             else:
#                 print(f'{number}', end=' ')
#                 number = number + 1
#         print()
#
# F_Triangle()
#           1
#         1 2 1
#        1 3 3 1
#       1 4 6 4 1
#
# def P_Triangle():
#     rows = int(input('Enter number of rows: '))
#     list1 = []
#     for i in range(rows):
#         temp_list = []
#         for j in range(i+1):
#             if j == 0 or j == i:
#                 temp_list.append(1)
#             else:
#                 temp_list.append(list1[i - 1][j-1] + list1[i-1][j])
#         list1.append(temp_list)
#     for i in range(rows):
#         for j in range(rows - i - 1):
#             print(' ', end='')
#         for j in range(rows):
#             print(list1[i][j], end=' ')
#         print()
# P_Triangle()


# def bit_length(self):
#     s = bin(self)
#     s = s.lstrip('-0b')
#     return len(s)
# print(bit_length(-37))
# x = '-24080928'
# print(x.lstrip('-24'))  # remove unnecessary numbers from left to right.

#
# # Program which counts the number of bits 1
# def BitCount(self):
#     return bin(self).count('1')  # counts the number of ones in binary representations of self value
# print(BitCount(19))
#
# print(int(129).to_bytes())


# lst = ['2', '5', '6', '8', '4', '7']
# max1 = max(lst)
# lst.remove(max1)
# print(max(lst))
# print(len(lst))
# greatest = lst[0]
# for i in range(1, len(lst)+1):
#     if greatest < lst[i]:
#         greatest = lst[i]
#
# print(greatest, 'was removed')
# lst.pop(lst.index(f'8'))
# print(' '.join(lst))
# greatest = lst[0]
# for i in range(1, len(lst)):
#     if greatest < lst[i]:
#         greatest = lst[i]
# print(greatest)

import math


# name = input('Введите имя: ').lower()
#vov = ['а', 'о', 'и', 'ы', 'у', 'э'] # гласные
# cons = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']  # Согласные
# const = []
# v, c = 0, 0
# for i in cons:
#     const.append(i.lower())
# for i in name:
#     if i in vov:
#         v = v + 1
#     else:
#         c = c + 1
# print(f'В имени {v} гласных и {c} согласных букв')



# s = 'AAAAAAABBBBCCCCCCCCDDD'
# x = []
# al = ['A', 'B', 'C', 'D']
# for i in al:
#     if i in s:
#         x.append(str(s.count(f'{i}')) + i)
# print(''.join(x))











