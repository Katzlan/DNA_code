
DNA_drosophila = str()

with open('DNA_drosophila.txt') as f:
  for line in f:
    DNA_drosophila += line
    
# Первый ген
gen_1 = str()
with open('LOC120285224.txt') as f: 
  for line in f:
    gen_1 += line
    
# Второй ген
gen_2 = str()
with open('LOC123327324.txt') as f: 
  for line in f:
    gen_2 += line
    
# Третий ген
gen_3 = str()
with open('LOC123327327.txt') as f: 
  for line in f:
    gen_3 += line
    
# Выдергиваю три гена из самой ДНК
DNA_fragment_find_1 = DNA_drosophila.rfind(gen_1)
DNA_fragment_find_2 = DNA_drosophila.rfind(gen_2)
DNA_fragment_find_3 = DNA_drosophila.rfind(gen_3)

# исправлено редактированием через Notepad++ текста до 1 строки
print(DNA_fragment_find_1, DNA_fragment_find_2, DNA_fragment_find_3)

# cоздаю текстовый док для записи фрагментов
f2 = open('DNA_fragments.txt', 'w')  
k = str({DNA_fragment_find_1, DNA_fragment_find_2, DNA_fragment_find_3})
f2.write('DNA_fragments:' + k)
f2.close()
