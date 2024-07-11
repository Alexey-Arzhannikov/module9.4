from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

#1
print('Задание №1')
my_func = list(map(lambda x, y: x == y, first, second))
print(my_func)

#2
print('Задание №2')
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='UTF-8') as file:
            for line in data_set:
                file.write(str(line))
                file.write('\n')
                print(line)
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], (12, 6), True)

#3
print('Задание №3')


class MysticBall:
    def __init__(self, *words):
        self.word = words

    def __call__(self):
        words = choice(self.word)
        return words


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Скорее да', 'Скорее нет')
for i in range(0, 11):
    print(first_ball())
