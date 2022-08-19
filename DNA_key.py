# -*- coding: utf-8 -*-
"""Ignatov.A.S._4_Kurz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A0dyTtghwO9r-LncCLhXa4IUruyzOyx4

ДЗ:

1. найти фрагмент ДНК в базах данных
2. составить алгоритм для ДНК-ключа и для поиска зашифрованной в ДНК информации с помощью ЭФ
3. написать код этого алгоритма
4. База данных: NCBI genome

ДНК-ключ - содержит инфо об остальном ДНК, в каком фрагменте расщепленного днк есть необходимая инфа (должен быть самым первым на ЭФ)
есть какие-то гены в фрагментах. Нужно провести ЭФ чтоб разделить на части и среди этих частей найти что-то, но мы ничего не знаем - нужен днк-ключ

Алгоритм для ДНК-ключа и для поиска зашифрованной в ДНК информации с помощью ЭФ

1. взять пару генов в геноме Drosophila simulans =  LOC120285224, LOC123327324, LOC123327327
2. определить эти гены 
3. cоздать ДНК-ключ
4. определиться с инструментами
5. определиться с форматом данных
////
N. написать код для поиска зашифрованнной в ДНК информации
"""

# Cама ДНК

DNA_drosophila = str()

with open('DNA_drosophila.txt') as f:
  for line in f:
    DNA_drosophila += line

print(len(DNA_drosophila)) # len(DNA_drosophila) = 1146867
print(DNA_drosophila)

# Первый ген

gen_1 = str()

with open('LOC120285224.txt') as f: 
  for line in f:
    gen_1 += line

print(len(gen_1)) # len(gen_1) = 6412
print(gen_1)

# Второй ген

gen_2 = str()

with open('LOC123327324.txt') as f: 
  for line in f:
    gen_2 += line

print(len(gen_2)) # len(gen_2) = 1524
print(gen_2)

# Третий ген

gen_3 = str()

with open('LOC123327327.txt') as f: 
  for line in f:
    gen_3 += line

print(len(gen_3)) # len(gen_3) = 2512
print(gen_3)

# Выдергиваю три гена из самой ДНК
# Отличие .find/.rfind - если представить слово 'hello', то при попытке .find(l) будет 2, в .rfind(l) будет 3. Cлово состоит из 5 символов. 
# Это помогает нам найти основное пространство, из которого выдернули какую-то часть. В нашем случае я выдернул gen_n из DNA_drosophila

DNA_fragment_find_1 = DNA_drosophila.rfind(gen_1)
DNA_fragment_find_2 = DNA_drosophila.rfind(gen_2)
DNA_fragment_find_3 = DNA_drosophila.rfind(gen_3)

print(DNA_fragment_find_1, DNA_fragment_find_2, DNA_fragment_find_3) # исправлено редактированием через Notepad++ текста до 1 строки

f2 = open('DNA_fragments.txt', 'w')  # cоздаю текстовый док для записи фрагментов
k = str({DNA_fragment_find_1, DNA_fragment_find_2, DNA_fragment_find_3})

f2.write('DNA_fragments:' + k)
f2.close()

"""Алгоритм для ДНК-ключа и для поиска зашифрованной в ДНК информации с помощью ЭФ

1. взять пару генов в геноме Drosophila simulans =  LOC120285224, LOC123327324, LOC123327327 **v**
2. определить эти гены **v**
3. cоздать ДНК-ключ **v**
4. определиться с инструментами open,input, .write/.close **v**
5. определиться с форматом данных => .txt **v**
////
N. написать код для поиска зашифрованнной в ДНК информации **v**
"""