"""
Напишите comprehension, который итерирует строку “1_2,40_5,5_32” (разбить по запятым) и
каждый элемент разбивает по символу “_” и полученные элементы приводит к типу int, и складывает их, тем самым образуя список целых чисел
"""
text = '1_2,40_5,5_32'
l = [int(x) for x in text.split(',') for x in x.split('_')]
print(l)