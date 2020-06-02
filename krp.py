import numpy as np

'''
клас, який описує символи
self.value - сам символ
self.amount - кількість відповідних символів у тексті 
self.pribability - ймовірність появи символу 
'''
class Symbol:
    
    def __init__(self,value):
        self.value = value
        self.amount = 0
        self.probability = 0

'''
функція що генерує список об'єктів класу Symbol

symbset - множина символів
res - список об'єктів класу Symbol
'''
def arr_of_cl(symbset):
    res = []
    for symbol in symbset:
        res.append(Symbol(symbol))
    return res

'''
функція що обчислює ентропію тексту
(При обчисленні Ентропії ймовірність появи символу
визначається як [кількість входжень у текст]/[загальна кількість символів])

text - текст який потрібно проаналізувати
bit_per_symb - число бітів на символ, потрібне для його кодування
'''
def entropy(text):
    textarr = list(text)
    symbset = set(textarr)
    clssarr = arr_of_cl(symbset)
    print("кількість символів: ",len(textarr))

    for symbol in textarr:
        for scl in clssarr:
            if symbol == scl.value:
                scl.amount += 1

    for scl in clssarr:
        scl.probability = scl.amount / len(textarr)

    bit_per_symb = 0
    for scl in clssarr:
        bit_per_symb -= scl.probability * np.log2(scl.probability)
    print("Ентропія: ",bit_per_symb)

    over = bit_per_symb - bit_per_symb // 1
    if over != 0:
        bit_per_symb = (bit_per_symb // 1) + 1


    print("Число бітів на символ: ",bit_per_symb)
    print("Ентропія тексту: ",int(bit_per_symb * len(textarr)))

f_eng = open("kafka_eng.txt", "r")
f_ukr = open("kafka_ukr.txt", "r")

text_eng = f_eng.read()
text_ukr = f_ukr.read()

f_eng.close()
f_ukr.close()

print("англійська версія тексу:")
entropy(text_eng)
print("\nукраїнська версія тексту: ")
entropy(text_ukr)
