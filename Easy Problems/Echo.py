"""
Эхо
Выведите длинное эхо - строку повторенную n раз.

Входные данные
Вводится строка и целое число - каждое на отдельной строке.

Выходные данные
Выводится эта же строка n раз через пробел.

Sample Input:
Ау
100

Sample Output:
Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау
Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау
Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау Ау
"""

class Echo:
    def __init__(self, repeat='Ау', times=100):
        self.repeat = repeat
        self.times = times
        
    def repeater(self):
        for _ in range(self.times):
            print(self.repeat, end=' ')
            

word = input()
number = int(input())
phrase = Echo(word, number)
phrase.repeater()
