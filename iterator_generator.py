from my_iterator import FlatIterator
from my_generator import flat_generator

#Проверка работоспособности итератора:
z = FlatIterator([
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
])

iterator_res = [x for x in z]
print (iterator_res)

#Проверка работоспособности генератора:
y = flat_generator([
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
])

generator_res = [x for x in y]
print (generator_res)