"""
Расстояние
Напишите программу которая вычисляет расстояние (км) по времени (ч) и скорости (км/ч).

Входные данные
С клавиатуры вводится два целых числа - каждое на отдельной строке.

Выходные данные
Вывести одно целое число - расстояние (км).

Sample Input:
5
15

Sample Output:
75
"""

class Distance:
    def __init__(self, time, speed):
        self.time = time
        self.speed = speed
        
    def find_distance(self) -> None:
        print(self.time * self.speed)
        
        
time: int = int(input())
speed: int = int(input())
    
path = Distance(time, speed)
path.find_distance()
