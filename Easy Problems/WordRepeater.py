"""
Столько раз сколько букв
Напишите программу которая повторяет введенную строку столько раз, сколько букв в этой строке.

Входные данные
Вводится одна строка.

Выходные данные
Выводится одна строка.

Sample Input 1:
hello

Sample Output 1:
hellohellohellohellohello
"""

class WordRepeater:
    def __init__(self, word):
        self.word = word
        
    def repeater(self):
        return self.word * len(self.word)
    

text = input()
message = WordRepeater(text)
print(message.repeater())
